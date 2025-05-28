import json
from collections import defaultdict

# 翻译字典，包含更多的常用术语和示例JSON内容中的描述
translation_map = {
    "question": "问题",
    "subtask": "子任务",
    "role": "角色",
    "content": "内容",
    "model_answer": "模型回答",
    "ground_truth": "真实答案",
    "success": "成功",
    "attempts": "尝试次数",
    "task_id": "任务ID",
    "level": "级别",
    "score": "得分",
    "trajectory": "轨迹",
    "subtasks_history": "子任务历史",
    "assignee_id": "被分配者ID",
    "worker_nodes": "工作节点",
    "capabilities": "能力",
    "tools": "工具",
    "helpful assistant": "有用的助手",
    "description": "描述",
    "coordinator": "协调器",
    "task_planner": "任务规划器",
    "assistant": "助手", # 模型的默认角色通常是assistant
    # 示例描述的翻译
    "Specialized in reasoning, coding, and processing excel files. However, it cannot access the internet to search for information. If the task requires python execution, it should be informed to execute the code after writing it.": "专注于推理、编码和处理Excel文件。然而，它无法访问互联网进行信息搜索。如果任务需要Python执行，应在编写代码后通知其执行。",
    "A helpful assistant that can process a variety of local and remote documents, including pdf, docx, images, audio, and video, etc.": "一个有用的助手，可以处理各种本地和远程文档，包括PDF、DOCX、图像、音频和视频等。",
    "A helpful assistant that can answer questions by searching the internet for information, processing web pages, performing actions, and retrieve relevant information.": "一个有用的助手，可以通过搜索互联网信息、处理网页、执行操作和检索相关信息来回答问题。",
    "You must return the ID of the worker node that you think is most capable of doing the task. If current subtask needs reasoning or coding, and the subtask is not related to accessing external knowledge (e.g. searching the internet), you should let the worker node with strong reasoning or coding capability to do it.": "你必须返回你认为最能胜任此任务的工作节点ID。如果当前子任务需要推理或编码，并且子任务与访问外部知识（例如搜索互联网）无关，则应让具有强大推理或编码能力的工作节点来完成。",
    "Open the provided Excel file located at data/gaia/2023/validation/32102e3e-d12a-4209-9163-7b3a104efe5d.xlsx to access the inventory data for the movie and video game rental store.": "打开位于 data/gaia/2023/validation/32102e3e-d12a-4209-9163-7b3a104efe5d.xlsx 的Excel文件，以访问电影和视频游戏租赁店的库存数据。",
    "Based on the inventory data, identify the column that contains the recording format (e.g., Blu-Ray, DVD, VHS).": "根据库存数据，识别包含录制格式（例如蓝光、DVD、VHS）的列。",
    "Filter the inventory data to only include entries where the format is 'Blu-Ray'.": "过滤库存数据，只包含格式为“蓝光”的条目。",
    "From the filtered Blu-Ray entries, locate the column that indicates the recording date or release year of the titles.": "从过滤后的蓝光条目中，找到指示标题录制日期或发布年份的列。",
    "Find the entry with the earliest recording date/release year among the Blu-Ray titles.": "在蓝光标题中找到录制日期/发布年份最早的条目。",
    "Extract the title of the oldest Blu-Ray as it appears in the spreadsheet.": "提取最旧的蓝光标题，其显示方式应与电子表格中一致。",
    "The attached spreadsheet shows the inventory for a movie and video game rental store in Seattle, Washington. What is the title of the oldest Blu-Ray recorded in this spreadsheet? Return it as appearing in the spreadsheet. Here are the necessary table files: data/gaia/2023/validation/32102e3e-d12a-4209-9163-7b3a104efe5d.xlsx, for processing excel file, you can write python code and leverage excel toolkit to process the file step-by-step and get the information.": "附件中的电子表格显示了华盛顿州西雅图一家电影和视频游戏租赁店的库存。此电子表格中记录的最旧的蓝光影片的标题是什么？请按电子表格中的显示返回。以下是必要的表格文件：data/gaia/2023/validation/32102e3e-d12a-4209-9163-7b3a104efe5d.xlsx，要处理Excel文件，你可以编写python代码并利用excel工具包逐步处理文件并获取信息。",
    "Time-Parking 2: Parallel Universe": "时光停车2：平行宇宙",
    # 工具名称的翻译
    "search_google": "谷歌搜索",
    "search_wiki": "维基搜索",
    "search_wiki_revisions": "维基修订搜索",
    "search_archived_webpage": "搜索存档网页",
    "extract_document_content": "提取文档内容",
    "browse_url": "浏览URL",
    "ask_question_about_video": "询问视频相关问题",
    "ask_question_about_image": "询问图片相关问题",
    "ask_question_about_audio": "询问音频相关问题",
    "execute_code": "执行代码",
    "extract_excel_content": "提取Excel内容"
}

def translate_text(text):
    """
    一个更健壮的翻译函数，处理更复杂的嵌套结构。
    """
    if isinstance(text, str):
        return translation_map.get(text, text)
    elif isinstance(text, dict):
        return {translate_text(k): translate_text(v) for k, v in text.items()}
    elif isinstance(text, list):
        return [translate_text(elem) for elem in text]
    else:
        return text

def process_data(data):
    """
    处理JSON数据，进行翻译并按task_id分组。
    这个函数现在会更深入地遍历所有嵌套结构。
    """
    translated_data = []
    for item in data:
        new_item = {}
        for key, value in item.items():
            if key == "task_id":
                new_item[key] = value # Task ID is kept as is for grouping
            elif key == "trajectory":
                translated_trajectory = []
                for attempt_item in value:
                    new_attempt_item = {}
                    for attempt_key, attempt_value in attempt_item.items():
                        if attempt_key == "trajectory": # This is the inner 'trajectory' array
                            inner_trajectory = []
                            for inner_step in attempt_value:
                                new_inner_step = {}
                                for step_key, step_value in inner_step.items():
                                    if step_key == "subtasks_history":
                                        subtasks_history = []
                                        for subtask_entry in step_value:
                                            translated_subtask_entry = {}
                                            for sub_key, sub_value in subtask_entry.items():
                                                if sub_key == "messages":
                                                    messages = []
                                                    for message_entry in sub_value:
                                                        new_message_entry = {}
                                                        for msg_key, msg_value in message_entry.items():
                                                            # Attempt to parse content if it's a JSON string, then translate
                                                            if msg_key == "content" and isinstance(msg_value, str):
                                                                try:
                                                                    parsed_content = json.loads(msg_value)
                                                                    # Recursively translate the parsed content
                                                                    translated_parsed_content = translate_text(parsed_content)
                                                                    new_message_entry[translate_text(msg_key)] = json.dumps(translated_parsed_content, ensure_ascii=False)
                                                                except json.JSONDecodeError:
                                                                    # If not a JSON string, just translate as normal text
                                                                    new_message_entry[translate_text(msg_key)] = translate_text(msg_value)
                                                            else:
                                                                new_message_entry[translate_text(msg_key)] = translate_text(msg_value)
                                                        messages.append(new_message_entry)
                                                    translated_subtask_entry[translate_text(sub_key)] = messages
                                                elif sub_key == "worker_nodes":
                                                    # Recursively translate worker_nodes and their nested content
                                                    translated_subtask_entry[translate_text(sub_key)] = translate_text(sub_value)
                                                else:
                                                    translated_subtask_entry[translate_text(sub_key)] = translate_text(sub_value)
                                            subtasks_history.append(translated_subtask_entry)
                                        new_inner_step[translate_text(step_key)] = subtasks_history
                                    else:
                                        new_inner_step[translate_text(step_key)] = translate_text(step_value)
                                inner_trajectory.append(new_inner_step)
                            new_attempt_item[translate_text(attempt_key)] = inner_trajectory
                        else:
                            new_attempt_item[translate_text(attempt_key)] = translate_text(attempt_value)
                    translated_trajectory.append(new_attempt_item)
                new_item[translate_text("trajectory")] = translated_trajectory
            else:
                new_item[translate_text(key)] = translate_text(value)
        translated_data.append(new_item)

    # Group by task_id
    grouped_tasks = defaultdict(list)
    for item in translated_data:
        grouped_tasks[item["task_id"]].append(item)
    return grouped_tasks


def generate_html(grouped_tasks):
    """
    生成HTML报告。
    确保完整渲染所有层级和智能体交互。
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI多智能体任务记录</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 20px; background-color: #f4f7f6; color: #333; line-height: 1.6; }
            .container { max-width: 1200px; margin: auto; background: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 6px 12px rgba(0,0,0,0.15); }
            h1 { color: #0056b3; text-align: center; margin-bottom: 30px; font-size: 2.5em; }
            .task-selector { text-align: center; margin-bottom: 20px; padding: 15px; background-color: #e6f7ff; border-radius: 8px; border: 1px solid #91d5ff; }
            .task-selector select { padding: 10px 15px; border-radius: 5px; border: 1px solid #91d5ff; font-size: 16px; width: 300px; max-width: 90%; background-color: #fff; cursor: pointer; }
            .task-section { display: none; border: 1px solid #e0e0e0; border-radius: 8px; margin-bottom: 30px; padding: 20px; background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
            .task-section.active { display: block; }
            h2 { color: #007bff; border-bottom: 3px solid #007bff; padding-bottom: 10px; margin-top: 25px; font-size: 2em; }
            h3 { color: #333; margin-top: 20px; font-size: 1.5em; border-bottom: 1px dashed #ccc; padding-bottom: 5px; }
            h4 { color: #555; margin-top: 15px; font-size: 1.2em; }
            .section-header { background-color: #f0faff; padding: 10px 15px; border-radius: 5px; margin-bottom: 15px; border-left: 5px solid #007bff; }
            .details { background-color: #f9f9f9; border-left: 5px solid #007bff; padding: 15px; margin-bottom: 15px; border-radius: 5px; }
            .interaction-flow { display: flex; flex-direction: column; gap: 15px; margin-top: 20px; }
            .flow-step { display: flex; align-items: flex-start; margin-bottom: 15px; }
            .flow-icon { font-size: 2em; margin-right: 15px; min-width: 40px; text-align: center; } /* Add min-width and text-align for consistent icon alignment */
            .flow-content { flex-grow: 1; padding: 10px 15px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }

            .coordinator-message .flow-content { background-color: #e0f7fa; border-left: 5px solid #00acc1; } /* Cyan darker */
            .task-planner-message .flow-content { background-color: #e8f5e9; border-left: 5px solid #66bb6a; } /* Green lighter */
            .worker-message .flow-content { background-color: #fff3e0; border-left: 5px solid #ffb74d; } /* Amber lighter */
            .system-message .flow-content { background-color: #e0e0e0; border-left: 5px solid #9e9e9e; } /* Grey */
            .user-message .flow-content { background-color: #e3f2fd; border-left: 5px solid #42a5f5; } /* Blue lighter */

            .assigned-task { background-color: #d4edda; border-color: #28a745; font-weight: bold; padding: 8px; border-radius: 4px; margin-bottom: 5px; } /* Success green */

            .subtask-item { background-color: #f0f8ff; border: 1px solid #cce5ff; margin-bottom: 15px; padding: 15px; border-radius: 8px; }
            .message-block { background-color: #ffffff; border: 1px solid #ddd; padding: 10px; margin: 10px 0; border-radius: 5px; } /* Changed to plain white for specific blocks */
            pre { background-color: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; white-space: pre-wrap; word-wrap: break-word; font-size: 0.9em; }
            strong { color: #0056b3; }
            table { width: 100%; border-collapse: collapse; margin-top: 15px; }
            th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
            th { background-color: #f2f2f2; color: #555; }
            .worker-node-info { background-color: #fff8e1; border: 1px solid #ffe082; padding: 15px; margin-top: 15px; border-radius: 8px; }
            .worker-node-info h5 { color: #8d6e63; margin-top: 0; border-bottom: 1px dotted #d7ccc8; padding-bottom: 5px; margin-bottom: 10px;}
            .worker-node-info ul { list-style: disc; padding-left: 20px; } /* Changed to disc list */
            .worker-node-info li { margin-bottom: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI多智能体任务记录</h1>

            <div class="task-selector">
                <label for="taskSelect">选择任务ID: </label>
                <select id="taskSelect" onchange="showTask()">
                    <option value="">请选择一个任务</option>
    """

    # We need to sort task_ids for consistent display in the dropdown
    sorted_task_ids = sorted(grouped_tasks.keys())
    for task_id in sorted_task_ids:
        html_content += f'<option value="task-{task_id}">{task_id}</option>'

    html_content += """
                </select>
            </div>
    """

    for task_id in sorted_task_ids: # Iterate through sorted keys
        tasks = grouped_tasks[task_id]
        for task in tasks: # Assuming one task per task_id in this structure for simplicity, if multiple, they'd appear sequentially
            html_content += f'<div id="task-{task_id}" class="task-section">'
            html_content += f'<h2>任务ID: {task_id}</h2>'

            # Task Level Details
            html_content += '<div class="section-header"><h3>任务概览</h3></div>'
            html_content += '<div class="details">'
            html_content += f'<p><strong>问题:</strong> {task.get("问题", "N/A")}</p>'
            html_content += f'<p><strong>级别:</strong> {task.get("级别", "N/A")}</p>'
            html_content += f'<p><strong>模型回答:</strong> {task.get("模型回答", "N/A")}</p>'
            html_content += f'<p><strong>真实答案:</strong> {task.get("真实答案", "N/A")}</p>'
            html_content += f'<p><strong>得分:</strong> {"成功" if task.get("得分") else "失败"}</p>' # Better wording for boolean score
            html_content += f'<p><strong>尝试次数:</strong> {task.get("尝试次数", "N/A")}</p>'
            html_content += '</div>'

            # Trajectory - This outer trajectory is for attempts
            if "轨迹" in task:
                html_content += '<div class="section-header"><h3>任务执行轨迹 (尝试)</h3></div>'
                for attempt_num, attempt in enumerate(task["轨迹"]):
                    html_content += f'<h4>尝试 {attempt_num + 1} 结果:</h4>'
                    html_content += '<div class="details">'
                    html_content += f'<p><strong>模型回答:</strong> {attempt.get("模型回答", "N/A")}</p>'
                    html_content += f'<p><strong>真实答案:</strong> {attempt.get("真实答案", "N/A")}</p>'
                    html_content += f'<p><strong>成功:</strong> {"是" if attempt.get("成功") else "否"}</p>'
                    html_content += f'<p><strong>尝试次数:</strong> {attempt.get("尝试次数", "N/A")}</p>'
                    html_content += '</div>'

                    if "轨迹" in attempt: # This inner trajectory represents the detailed steps within an attempt
                        html_content += '<div class="section-header"><h5>子任务执行流程与智能体交互</h5></div>'
                        html_content += '<div class="interaction-flow">'
                        for sub_exec_num, sub_exec in enumerate(attempt["轨迹"]): # Iterate through steps within an attempt
                            if "子任务历史" in sub_exec:
                                for subtask_hist_num, subtask_hist in enumerate(sub_exec["子任务历史"]):
                                    html_content += f'<div class="subtask-item">'
                                    html_content += f'<h4>子任务 {subtask_hist_num + 1}: {subtask_hist.get("子任务", "N/A")}</h4>'

                                    if "messages" in subtask_hist:
                                        html_content += '<h5>消息交互:</h5>'
                                        for msg_num, message in enumerate(subtask_hist["messages"]):
                                            role = message.get("角色", "system").lower()
                                            content = message.get("内容", "N/A")
                                            message_class = ""
                                            icon = "💬" # Default icon

                                            # Assign CSS class and icon based on role
                                            if role == "coordinator":
                                                message_class = "coordinator-message"
                                                icon = "⚙️"
                                            elif role == "task_planner":
                                                message_class = "task-planner-message"
                                                icon = "🧠"
                                            elif role == "assistant": # This is typically the worker agent's response
                                                message_class = "worker-message"
                                                icon = "👷"
                                            elif role == "user": # Added user role handling
                                                message_class = "user-message"
                                                icon = "👤"
                                            else:
                                                message_class = "system-message"
                                                icon = "🖥️"

                                            html_content += f'<div class="flow-step {message_class}">'
                                            html_content += f'<div class="flow-icon">{icon}</div>'
                                            html_content += '<div class="flow-content">'
                                            html_content += f'<strong>{translate_text(role).capitalize()}:</strong><br>'
                                            try:
                                                parsed_content = json.loads(content)
                                                if isinstance(parsed_content, dict) and "assignee_id" in parsed_content:
                                                    html_content += f'<p class="assigned-task"><strong>任务分配:</strong> 将任务分配给工作节点 <code>{parsed_content["assignee_id"]}</code></p>'
                                                    html_content += f'<p><strong>完整内容:</strong></p><pre>{json.dumps(parsed_content, indent=2, ensure_ascii=False)}</pre>'
                                                else:
                                                    html_content += f'<p><strong>内容:</strong></p><pre>{json.dumps(parsed_content, indent=2, ensure_ascii=False)}</pre>'
                                            except (json.JSONDecodeError, TypeError):
                                                html_content += f'<p><strong>内容:</strong> <pre>{content}</pre></p>'
                                            html_content += '</div></div>'

                                    if "worker_nodes" in subtask_hist:
                                        html_content += '<h5>当前工作节点配置:</h5>'
                                        html_content += '<div class="worker-node-info">'
                                        for node_id, node_info in subtask_hist["worker_nodes"].items():
                                            html_content += f'<h6>工作节点 ID: {node_id}</h6>'
                                            html_content += f'<p><strong>描述:</strong> {node_info.get("描述", "N/A")}</p>'
                                            if "能力" in node_info:
                                                html_content += f'<p><strong>能力:</strong> {node_info["能力"]}</p>' # Assuming capabilities is a string from translation
                                            if "工具" in node_info:
                                                html_content += f'<ul><strong>工具:</strong>'
                                                for tool in node_info["工具"]:
                                                    html_content += f'<li>{tool}</li>'
                                                html_content += '</ul>'
                                        html_content += '</div>'
                                    html_content += '</div>' # End of subtask-item
                        html_content += '</div>' # End of interaction-flow div
            html_content += '</div>' # End of task-section div

    html_content += """
        </div>
        <script>
            function showTask() {
                var selectBox = document.getElementById("taskSelect");
                var selectedTaskId = selectBox.options[selectBox.selectedIndex].value;
                var taskSections = document.getElementsByClassName("task-section");

                for (var i = 0; i < taskSections.length; i++) {
                    taskSections[i].classList.remove("active");
                }

                if (selectedTaskId) {
                    var activeTaskSection = document.getElementById(selectedTaskId);
                    if (activeTaskSection) {
                        activeTaskSection.classList.add("active");
                    }
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

# --- 主执行部分 ---
if __name__ == "__main__":
    file_path = "/home/kaji/owl/results/workforce/workforce_1_pass1_gpt4o.json" # 确保文件名正确
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        grouped_data = process_data(json_data)
        html_output = generate_html(grouped_data)

        output_html_file = "workforce_tasks_report_full_details.html"
        with open(output_html_file, 'w', encoding='utf-8') as f:
            f.write(html_output)

        print(f"完整详细HTML报告已成功生成到: {output_html_file}")

    except FileNotFoundError:
        print(f"错误: 未找到文件 '{file_path}'。请确保文件与脚本在同一目录下。")
    except json.JSONDecodeError:
        print(f"错误: 无法解析文件 '{file_path}'。请检查JSON格式是否正确。")
    except Exception as e:
        print(f"发生未知错误: {e}")