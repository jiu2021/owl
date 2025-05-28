#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
@File   : llm_proxy_trace.py
@Time   : 2025/05/16 10:17
@Author : sunsongtao
@Email  : sunsongtao@wps.cn
@Desc   : LLM服务代理，并追踪请求和响应
"""

import http.server
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from http.client import HTTPMessage
from typing import Any, Dict, List, Optional

from langfuse.decorators import langfuse_context, observe
from langfuse.api.resources.ingestion.types.open_ai_completion_usage_schema import OpenAiCompletionUsageSchema
from loguru import logger

TARGET_LLM_API_BASE = os.getenv("TARGET_LLM_API_BASE", "https://aihubmix.com")
CLEAN_RESPONSE_HEADERS = [
    "accept-encoding",
    "transfer-encoding",
    "content-length",
    # "connection"
]
CLEAN_REQUEST_HEADERS = CLEAN_RESPONSE_HEADERS + ["host"]


def clean_request_headers(headers: HTTPMessage) -> Dict[str, str]:
    """清理请求头，移除不必要的头信息。"""
    ret_headers = {}
    for k, v in headers.items():
        if k.lower() in CLEAN_REQUEST_HEADERS:
            logger.debug(f"clean_request_header: {k} = {v}")
            continue
        ret_headers[k] = v

    return ret_headers


def _extract_streamed_openai_response(chunks: List[Any]):
    """提取流式回复的模型、使用情况和内容。"""
    completion = defaultdict(str)
    model, usage = None, None

    for chunk in chunks:
        if not isinstance(chunk, dict):
            logger.error(f"chunk is not a dict: {chunk}")
            continue

        model = model or chunk.get("model", None) or None
        usage = chunk.get("usage", None)

        choices = chunk.get("choices", [])

        for choice in choices:
            text = choice.get("text", None)
            reasoning_content = choice.get("reasoning_content", None)
            delta = choice.get("delta", None)
            if delta is None and (text or reasoning_content):
                # AI网关返回的流式回复，没有delta字段
                delta = {
                    "role": "assistant",
                    "content": text,
                    "reasoning_content": reasoning_content
                }

            if delta is None:
                logger.error(f"delta is None: {choice}")
                continue

            if delta.get("role", None) is not None:
                completion["role"] = delta["role"]

            if delta.get("content", None) is not None:
                completion["content"] = (
                    delta.get("content", None)
                    if completion["content"] is None
                    else completion["content"] + delta.get("content", None)
                )
            elif delta.get("reasoning_content", None) is not None:
                completion["reasoning_content"] = (
                    delta.get("reasoning_content", None)
                    if completion["reasoning_content"] is None
                    else completion["reasoning_content"] + delta.get("reasoning_content", None)
                )
            elif delta.get("function_call", None) is not None:
                curr = completion["function_call"]
                tool_call_chunk = delta.get("function_call", None)

                if not curr:
                    completion["function_call"] = {
                        "name": tool_call_chunk.get("name", ""),
                        "arguments": tool_call_chunk.get("arguments", ""),
                    }

                else:
                    curr["name"] = curr["name"] or tool_call_chunk.get(
                        "name", None
                    )
                    curr["arguments"] += tool_call_chunk.get("arguments", "")

            elif delta.get("tool_calls", None) is not None:
                curr = completion["tool_calls"]
                tool_call = delta.get("tool_calls", [{}])
                tool_call_chunk = tool_call[0].get("function", {})

                if not curr:
                    completion["tool_calls"] = [
                        {
                            "name": tool_call_chunk.get("name", ""),
                            "arguments": tool_call_chunk.get("arguments", ""),
                        }
                    ]

                elif tool_call_chunk.get("name", None) is not None:
                    curr.append(
                        {
                            "name": tool_call_chunk.get("name", None),
                            "arguments": tool_call_chunk.get("arguments", None),
                        }
                    )

                else:
                    curr[-1]["name"] = curr[-1]["name"] or tool_call_chunk.get(
                        "name", None
                    )
                    curr[-1]["arguments"] += tool_call_chunk.get(
                        "arguments", "")

    def get_response_for_chat():
        logger.debug(f"completion: {completion}")
        content = completion["content"]
        reasoning_content = completion["reasoning_content"]
        function_call = completion["function_call"]
        tool_calls = completion["tool_calls"]
        response = {"role": "assistant"}
        if reasoning_content:
            response["reasoning_content"] = reasoning_content
        if content:
            response["content"] = content
        if function_call:
            response["function_call"] = function_call
        if tool_calls:
            response["tool_calls"] = [
                {"function": data} for data in tool_calls
            ]

        return response

    return (
        model,
        get_response_for_chat(),
        usage,
        {"chunks": len(chunks)},
    )


@observe(name="request")
def _trace_post_request(content: bytes):
    """追踪POST请求。"""
    # TODO: 更健壮的解码处理
    request_body = content.decode("utf-8", "replace")
    try:
        body = json.loads(request_body)
    except json.JSONDecodeError:
        logger.error(f"json.JSONDecodeError: {request_body}")
        body = request_body

    msg = {"step": "request", "body": body}
    logger.debug(f"Request body: \n{msg}")
    langfuse_context.update_current_trace(
        input=body,
    )


@observe(name="response", as_type="generation")
def _trace_post_response(data_list: List[Any]):
    """追踪POST响应。"""
    if len(data_list) == 0:
        logger.error(f"data_list is empty")
        return

    msg = {"step": "response", "body": f"{len(data_list)} chunks"}
    logger.debug(f"Response body: \n{msg}")

    if not all(isinstance(data, dict) for data in data_list):
        # TODO: 是否区分具体接口（chat.completions.create 和 responses.create）？
        logger.warning(f"data_list is not a list of dicts: \n{data_list}")
        return

    if len(data_list) == 1:
        # 非流式回复
        response = data_list[0]
        metadata = response.get("metadata", {})
        metadata["model"] = response.get("model", None)
        metadata["usage"] = response.get("usage", None)
        choice = response.get("choices", [{}])[0]
        content = choice.get("message", {}).get("content", None)
        text = choice.get("text", None)
        if not content and text:
            content = text

        langfuse_context.update_current_trace(
            output=content,
            metadata=metadata,
        )
        langfuse_context.update_current_observation(
            output=content,
            usage_details=metadata["usage"],
        )
        return

    # 流式回复
    logger.debug(f"data_list[-5:]: {data_list[-5:]}")
    model, completion, usage, metadata = _extract_streamed_openai_response(
        data_list)
    logger.debug(f"completion[-100:]: {str(completion)[-100:]}")
    metadata["model"] = model
    metadata["usage"] = usage
    langfuse_context.update_current_trace(
        output=completion,
        metadata=metadata
    )
    langfuse_context.update_current_observation(
        output=completion,
        usage_details=usage,
    )


class OpenAIProxyHandler(http.server.BaseHTTPRequestHandler):

    def _create_target_request(self, method: str, body: bytes, headers: Dict[str, str]):
        """创建目标LLM服务请求"""
        target_url = TARGET_LLM_API_BASE + self.path
        req = urllib.request.Request(
            target_url,
            data=body if body else None,
            headers=headers,
            method=method
        )
        return req

    def _forward_then_response(self, req: urllib.request.Request, method: str):
        """将请求转发到目标URL并处理响应。"""
        with urllib.request.urlopen(req) as response:
            self.send_response(response.status)
            resp_headers = response.getheaders()
            logger.debug(f"resp_headers: \n{resp_headers}")
            for header, value in resp_headers:
                if header.lower() in CLEAN_RESPONSE_HEADERS:
                    logger.debug(f"clean_response_header: {header} = {value}")
                    continue
                self.send_header(header, value)
            # self.send_header("Cache-Control", "no-cache")
            self.end_headers()

            if method != "POST":
                # 非POST请求，直接返回响应
                logger.info(f"Non-POST request, return response directly.")
                self.wfile.write(response.read())
                return

            # 处理POST请求的回复（可能是流式的）
            self._process_and_forward_data(response)

    def _process_and_forward_data(self, response):
        """处理并转发回复数据。"""
        data_list = []
        while True:
            line = response.readline()
            if not line:
                logger.info(f"Line is empty, break.")
                break

            # TODO: 更健壮的解码处理
            line = line.decode("utf-8").strip()
            if not line:
                continue

            # 处理每行数据
            if line.startswith("data:"):
                # 流式回复
                content = line[5:].strip()
            else:
                # 非流式回复
                content = line
                logger.debug(f"Non-stream response: {content}")

            if content.lower() == "[done]":
                # 流式回复结束
                logger.debug(f"data: [DONE]")
                self.wfile.write(b"data: [DONE]\n")
                self.wfile.flush()
                break

            try:
                data = json.loads(content)
                data_list.append(data)
            except json.JSONDecodeError:
                logger.error(f"json.JSONDecodeError: {content}")
                data_list.append(content)

            obv_token = "Observation:"
            if line.startswith("data:") and obv_token in line:
                # FIXME: 触发ReACT的Observation幻觉（仅处理流式回复）
                logger.warning(f"Hit ReACT observation: {line}")
                self.wfile.write((line + "\n\n").encode("utf-8"))
                self.wfile.write(b"data: [DONE]\n")
                self.wfile.flush()
                break

            self.wfile.write((line + "\n\n").encode("utf-8"))
            self.wfile.flush()

        # 记录回复数据
        _trace_post_response(data_list)

    def _handle_request(self, method: str, body: Optional[bytes] = None):
        """将请求转发到目标URL并处理响应。"""
        req_headers = clean_request_headers(self.headers)

        try:
            # 创建目标LLM服务请求
            req = self._create_target_request(method, body, req_headers)
            # 执行请求转发和回复处理的代理逻辑
            self._forward_then_response(req, method)

        except urllib.error.HTTPError as e:
            # 处理HTTP错误，返回目标接口的详细错误信息
            explain = "LLM服务异常"
            if hasattr(e, "read"):
                logger.debug(f"e.headers: {e.headers}")
                # TODO: 更健壮的解码处理
                explain = e.read().decode("utf-8", "replace")

            self.send_error(e.code, e.reason, str(explain))
        except Exception as e:
            # 处理其他异常，返回500错误
            self.send_error(500, str(e))

    def do_GET(self):
        """处理GET请求。"""
        logger.debug(f"GET headers:\n{self.headers}")
        self._handle_request("GET")

    def do_OPTIONS(self):
        """处理OPTIONS请求。"""
        logger.debug(f"OPTIONS headers:\n{self.headers}")
        self._handle_request("OPTIONS")

    @observe(name="llm_proxy_post")
    def do_POST(self):
        """处理POST请求。"""
        logger.debug(f"POST headers:\n{self.headers}")
        langfuse_context.update_current_trace(
            metadata={
                "client_address": self.client_address
            }
        )

        request_id = self.headers.get("Client-Request-Id", None)
        if request_id:
            logger.debug(f"Client-Request-Id: {request_id}")
            langfuse_context.update_current_trace(
                session_id=request_id
            )
        topic_id = self.headers.get("Topic-Id", None)
        if topic_id:
            logger.debug(f"Topic-Id: {topic_id}")
            langfuse_context.update_current_trace(
                tags=[topic_id]
            )

        content_length = int(self.headers.get("Content-Length", 0))
        if content_length > 0:
            content = self.rfile.read(content_length)
            logger.debug(f"Read content length: {len(content)}")
            # 记录请求数据
            _trace_post_request(content)
        else:
            content = None

        self._handle_request("POST", body=content)


def run_server(port: int):
    server_address = ("0.0.0.0", port)
    httpd = http.server.HTTPServer(server_address, OpenAIProxyHandler)
    logger.info(f"启动服务器在端口：<{port}>")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        logger.warning("服务器已关闭")
    except Exception as e:
        logger.error(f"服务器启动失败: {e}")


if __name__ == "__main__":
    # 获取命令行参数
    try:
        port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    except ValueError:
        logger.warning("端口号格式错误，使用默认端口8000")
        port = 8000

    run_server(port)
