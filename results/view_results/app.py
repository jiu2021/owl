# app.py
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app) # Enable CORS for frontend development

DATA_FILE = '/home/kaji/owl/results/workforce/workforce_1_pass1_gpt4o.json'
tasks_data = {}

def load_data():
    """Loads the task data from the JSON file."""
    global tasks_data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Index data by task_id for easy lookup
            for task in data:
                tasks_data[task['task_id']] = task
        print(f"Loaded {len(tasks_data)} tasks from {DATA_FILE}")
        if tasks_data:
            first_task_id = next(iter(tasks_data))
            print(f"First loaded task_id: {first_task_id}")
            print(f"First task details (partial): {list(tasks_data[first_task_id].keys())}")
        else:
            print("No tasks loaded.")
    else:
        print(f"Error: {DATA_FILE} not found. Please make sure the JSON file is in the same directory as app.py.")

@app.before_request
def before_first_request():
    """Load data only once when the first request comes in."""
    if not tasks_data:
        load_data()

@app.route('/')
def index():
    """Renders the main frontend page."""
    return render_template('index.html')

@app.route('/api/task_ids')
def get_task_ids():
    """Returns a list of all available task IDs."""
    return jsonify(list(tasks_data.keys()))

@app.route('/api/task/<task_id>')
def get_task_details(task_id):
    """Returns the details for a specific task ID, focusing on collaboration and main task info."""
    task = tasks_data.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    response_data = {
        "task_id": task.get("task_id"),
        "question": task.get("question", "N/A"),
        "model_answer": task.get("model_answer", "N/A"),
        "ground_truth": task.get("ground_truth", "N/A"),
        "score": task.get("score", False),
        "attempts_count": task.get("attempts", 0),
        "trajectory_attempts": []
    }

    if 'trajectory' in task and isinstance(task['trajectory'], list):
        for traj_idx, top_level_trajectory in enumerate(task['trajectory']):
            current_attempt_details = {
                "attempt_index": traj_idx,
                "attempt_success": top_level_trajectory.get("success", "N/A"),
                "attempt_model_answer": top_level_trajectory.get("model_answer", "N/A"),
                "attempt_ground_truth": top_level_trajectory.get("ground_truth", "N/A"),
                "steps": [] # This will contain all types of history entries
            }

            if 'trajectory' in top_level_trajectory and isinstance(top_level_trajectory['trajectory'], list):
                for step_idx, step_data in enumerate(top_level_trajectory['trajectory']):
                    # Process subtasks_history
                    if 'subtasks_history' in step_data and isinstance(step_data['subtasks_history'], list):
                        for subtask_history in subtask_history_to_messages(step_data['subtasks_history'], step_idx):
                            current_attempt_details["steps"].append(subtask_history)

                    # Process planner_history
                    if 'planner_history' in step_data and isinstance(step_data['planner_history'], list):
                        for planner_entry in process_agent_history(step_data['planner_history'], "Task Planner", step_idx):
                            current_attempt_details["steps"].append(planner_entry)

                    # Process coordinator_history
                    if 'coordinator_history' in step_data and isinstance(step_data['coordinator_history'], list):
                        for coordinator_entry in process_agent_history(step_data['coordinator_history'], "Coordinator", step_idx):
                            current_attempt_details["steps"].append(coordinator_entry)
            response_data["trajectory_attempts"].append(current_attempt_details)
    return jsonify(response_data)


def parse_message_content(content):
    """Attempts to parse JSON content from a message and format it."""
    try:
        json_content = json.loads(content)
        # Prioritize specific fields for display
        if "assignee_id" in json_content:
            return f"Assigned to Worker Node ID: {json_content['assignee_id']}"
        elif "tool_code" in json_content:
            return f"Tool Code Executed:\n{json_content.get('tool_code', 'N/A')}"
        elif "observation" in json_content:
            try: # Observation might be a JSON string itself
                obs_json = json.loads(json_content.get('observation', 'N/A'))
                return f"Observation:\n{json.dumps(obs_json, indent=2)}"
            except (json.JSONDecodeError, TypeError):
                return f"Observation: {json_content.get('observation', 'N/A')}"
        elif "tool_output" in json_content:
            return f"Tool Output:\n{json_content.get('tool_output', 'N/A')}"
        elif "answer" in json_content:
            return f"Final Answer: {json_content.get('answer', 'N/A')}"
        # Fallback to pretty-printed JSON if no specific field is found
        return json.dumps(json_content, indent=2)
    except json.JSONDecodeError:
        return content # Not a JSON string, return as is

def subtask_history_to_messages(history_list, step_idx):
    """Processes subtasks_history into a list of formatted messages."""
    processed_entries = []
    for entry in history_list:
        detail = {
            "type": "subtask_message", # Indicate this is a subtask message
            "subtask_step_index": step_idx,
            "subtask_description": entry.get("subtask", "N/A"),
            "messages": []
        }
        if 'messages' in entry and isinstance(entry['messages'], list):
            for msg in entry['messages']:
                if 'role' in msg and 'content' in msg:
                    detail["messages"].append({
                        "role": msg['role'],
                        "content": parse_message_content(msg['content'])
                    })
        processed_entries.append(detail)
    return processed_entries


def process_agent_history(history_list, agent_type, step_idx):
    """Processes planner_history or coordinator_history into a list of formatted messages."""
    processed_entries = []
    for msg in history_list:
        if 'role' in msg and 'content' in msg:
            detail = {
                "type": f"{agent_type.lower().replace(' ', '_')}_message", # e.g., "task_planner_message", "coordinator_message"
                "agent_type": agent_type, # e.g., "Task Planner", "Coordinator"
                "subtask_step_index": step_idx, # Associate with the step it occurred in
                "messages": [{
                    "role": msg['role'],
                    "content": parse_message_content(msg['content'])
                }]
            }
            processed_entries.append(detail)
    return processed_entries


if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)