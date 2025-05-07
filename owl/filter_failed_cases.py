import json
import os
from loguru import logger
from tqdm import tqdm
import requests
import html2text
import string
from typing import List, Dict
# use html2text to extract the text from the url


def find_failed_cases_id(failed_cases: List[Dict], reference_data_list: List[Dict]) -> List[str]:
    failed_cases_id = []
    for failed_case in failed_cases:
        for reference_case in reference_data_list:
            if failed_case['task_id'] == reference_case['task_id']:
                failed_cases_id.append(reference_case['idx'])
    return failed_cases_id


def check_invalid_answer(attempt_dict: dict, max_tries: int) -> bool:
    
    # if len(attempt_dict) != max_tries:
    #     return True
    
    model_answer_count = {}
    
    for attempt_answer in attempt_dict.values():
        if attempt_answer == "":
            attempt_answer = "None"
            
        if attempt_answer in model_answer_count:
            model_answer_count[attempt_answer] += 1
        else:
            model_answer_count[attempt_answer] = 1 
        
    max_count = max(model_answer_count.values())
    if max_count > 1:
        return False
    else:
        return True
 


def extract_text_from_url(url: str) -> str:
    response = requests.get(url)
    
    return html2text.html2text(response.text)


# check if the string can be encoded to utf-8
def check_containing_unprintable_characters(string: str) -> bool:
    tool_calling_information = extract_tool_calling_information(string)
    
    for tool_calling_info in tool_calling_information:
        if is_raw_binary_data(tool_calling_info):
            return True
    return False


def check_containing_failed_keywords(string: str) -> bool:
    # if the string contains any of the failed keywords, return False
    # otherwise, return True
    # failed_keywords = [
    #     "I was unable",
    #     "It seems",
    #     "I'm sorry",
    #     "I apologize",
    #     "I'm not sure",
    # ]
    failed_keywords = [
        "It seems",        
        "connection"
    ]
    
    for keyword in failed_keywords:
        if keyword.lower() in string.lower():
            return True
    return False



def extract_tool_calling_information(string: str) -> List[str]:
    """Consider the pattern like this:
    {
        "role": "tool",
        "content": "...",
        "tool_call_id": "..."
    }
    extract data between `"role": "tool"` and `"tool_call_id": "..."`
    The string may contain multiple tool calling information, return all of them one by one
    """
    
    tool_calling_information = []
    string = string.replace("'", '"')
    string = string.replace("\\", "")
    
    while True:
        start_index = string.find('"role": "tool"')
        if start_index == -1:
            break
        
        end_index = string.find('"tool_call_id": "', start_index)
        if end_index == -1:
            break
        
        tool_calling_information.append(string[start_index:end_index])
        
        string = string[end_index:]
    
    return tool_calling_information
    

def is_raw_binary_data(data: str, threshold: float = 0.05) -> bool:
    """
    check if the string is raw binary data
    """
    if not data:
        return False  # empty string is not binary data

    # string.printable contains digits, letters, punctuation, and some whitespace characters (e.g. space, newline)
    printable_chars = set(string.printable)
    
    # count the number of non-printable characters
    non_printable_count = sum(1 for ch in data if ch not in printable_chars)
    
    # count the ratio of non-printable characters
    non_printable_ratio = non_printable_count / len(data)
    
    # logger.info(f"The ratio of non-printable characters is {non_printable_ratio}")
    
    if non_printable_ratio > threshold:
        return True
    else:
        return False



def check_file(file_path: str):
    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    elif file_path.endswith(".jsonl"):
        with open(file_path, "r", encoding="utf-8") as f:
            data = [json.loads(line) for line in f]
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

    failed_cases = []

    for case in tqdm(data):
        
        if "trajectory" not in case:
            continue
        
        # all_trajectory = case['trajectory']
        task_failed = False
        
        rules = {
            "invalid_answer": False,
        }
        
        if check_invalid_answer(case['model_answer'], 3):  
            rules["invalid_answer"] = True
            task_failed = True
        
        # for one_trajectory in all_trajectory:
        #     all_text = str(one_trajectory)
            
        #     # check based on rules one by one
            
        #     if check_containing_failed_keywords(all_text):
        #         rules["contains_failed_keywords"] = True
                
        #     if check_containing_unprintable_characters(all_text):
        #         rules["contains_unprintable_characters"] = True
                

                
        #     # if any rule is violated, add the case to the failed cases
        #     for rule in rules:
        #         if rules[rule]:
        #             task_failed = True
        #             break         

        if task_failed:
            cases_info = {
                "task_id": case['task_id'],
                "question": case['question'],
                "level": case['level'],
                "model_answer": case['model_answer'],
                "ground_truth": case['ground_truth'],
                "rules": rules,
            }
            failed_cases.append(cases_info)
        
    logger.info(f"Found {len(failed_cases)} failed cases")
    for case in failed_cases:
        logger.info(f"Task index: {case['task_id']}")
        logger.info(f"Question: {case['question']}")
        logger.info(f"Model Answer: {case['model_answer']}")
        logger.info(f"Ground Truth: {case['ground_truth']}")
        logger.info(f"Rules: {case['rules']}")
        logger.info("-"*100)
    return failed_cases


if __name__ == "__main__":
    
    LEVEL = 1
    
    reference_data_path = f"../tasks/level_{LEVEL}_tasks_test.json"

    with open(reference_data_path, "r", encoding="utf-8") as f:
        reference_data_list = json.load(f)
    
    failed_cases = check_file(f"../results/workforce/workforce_{LEVEL}_test_pass3.json")
    
    failed_cases_id = find_failed_cases_id(failed_cases, reference_data_list)
    logger.info(f"Found {len(failed_cases)} failed cases")
    logger.info(f"Failed cases id: {failed_cases_id}")
    
    # with open("../results/test/test.json", "r", encoding="utf-8") as f:
    #     data = json.load(f)
    # data = str(data)
    # containing_unprintable_characters = check_containing_unprintable_characters(str(data))
    # print(containing_unprintable_characters)

