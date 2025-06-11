import os
import json

def find_task_in_workforce(task_id):
    root_dir = "/home/kaji/owl/results/workforce/"
    for i in range(1,4):
        workforce = os.path.join(root_dir, f'workforce_{i}_pass1_gpt4o.json')
        if os.path.exists(workforce):
            with open(workforce, 'r') as workforce:
                workforce_data = json.load(workforce)
                for task in workforce_data:
                    if task['task_id'] == task_id:
                        return i
    return None


def find_task(task_id):
    root_dir = "/home/kaji/owl/tasks/"
    for i in range(1,4):
        workforce = os.path.join(root_dir, f'level_{i}_tasks.json')
        if os.path.exists(workforce):
            with open(workforce, 'r') as workforce:
                workforce_data = json.load(workforce)
                for task in workforce_data:
                    if task['task_id'] == task_id:
                        return task['Level'], task['idx']
    return None




if __name__ == "__main__":
    for file in os.listdir("/home/kaji/owl/data/gaia/2023/validation/"):
        task_id = file.split('.')[0]
        file_type = file.split('.')[-1]
        # if file_type not in ['mp3', 'jpg', 'png']:
        #     continue
        workforce_res = find_task_in_workforce(task_id)
        if workforce_res is None:
            # print(f"Task ID: {task_id} not found in any workforce")
            task_res = find_task(task_id)
            if task_res is not None:
                print(f"Task ID: {task_id} found in Level {task_res[0]}, Index {task_res[1]}")