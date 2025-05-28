// templates/static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const taskSelect = document.getElementById('task-select');
    const fetchButton = document.getElementById('fetch-button');
    const visualizationArea = document.getElementById('visualization-area');
    const mainTaskInfoDiv = document.createElement('div');
    mainTaskInfoDiv.id = 'main-task-info';
    visualizationArea.insertBefore(mainTaskInfoDiv, visualizationArea.firstChild);

    const collaborationDetailsDiv = document.getElementById('collaboration-details');

    const API_BASE_URL = window.location.origin;

    async function populateTaskIds() {
        try {
            const response = await fetch(`${API_BASE_URL}/api/task_ids`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const taskIds = await response.json();
            taskIds.forEach(id => {
                const option = document.createElement('option');
                option.value = id;
                option.textContent = id;
                taskSelect.appendChild(option);
            });
        } catch (error) {
            console.error("Error fetching task IDs:", error);
            mainTaskInfoDiv.innerHTML = '';
            collaborationDetailsDiv.innerHTML = `<p style="color: red;">Error loading task IDs. Please ensure the server is running and the JSON file is accessible.</p>`;
        }
    }

    async function fetchCollaborationDetails(taskId) {
        mainTaskInfoDiv.innerHTML = '';
        collaborationDetailsDiv.innerHTML = '<p>Loading collaboration details...</p>';
        try {
            const response = await fetch(`${API_BASE_URL}/api/task/${taskId}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            renderMainTaskInfo(data);
            renderTrajectoryAttempts(data.trajectory_attempts);
        } catch (error) {
            console.error("Error fetching collaboration details:", error);
            mainTaskInfoDiv.innerHTML = '';
            collaborationDetailsDiv.innerHTML = `<p style="color: red;">Error loading collaboration details for task ID: ${taskId}.</p>`;
        }
    }

    function renderMainTaskInfo(data) {
        if (!data) return;

        mainTaskInfoDiv.innerHTML = `
            <h3>Task ID: ${data.task_id}</h3>
            <p><strong>Question:</strong> ${data.question}</p>
            <p><strong>Model Answer (Overall):</strong> ${data.model_answer}</p>
            <p><strong>Ground Truth (Overall):</strong> ${data.ground_truth}</p>
            <p><strong>Overall Success:</strong> ${data.score ? 'Success' : 'Failure'}</p>
            <p><strong>Total Attempts:</strong> ${data.attempts_count}</p>
            <hr/>
        `;
    }

    function renderTrajectoryAttempts(attempts) {
        if (!attempts || attempts.length === 0) {
            collaborationDetailsDiv.innerHTML = '<p>No detailed collaboration steps found for this task.</p>';
            return;
        }

        collaborationDetailsDiv.innerHTML = '';

        attempts.forEach((attempt, attemptIndex) => {
            const attemptSection = document.createElement('div');
            attemptSection.classList.add('attempt-section');

            const attemptHeader = document.createElement('h2');
            attemptHeader.textContent = `Trajectory Attempt ${attempt.attempt_index + 1} (${attempt.attempt_success ? 'Success' : 'Failure'})`;
            attemptSection.appendChild(attemptHeader);

            attemptSection.innerHTML += `
                <p><strong>Attempt Model Answer:</strong> ${attempt.attempt_model_answer}</p>
                <p><strong>Attempt Ground Truth:</strong> ${attempt.attempt_ground_truth}</p>
                <hr style="border-top: 1px dashed #ccc;">
            `;

            if (attempt.steps && attempt.steps.length > 0) {
                // Sort steps by their index to ensure chronological order
                attempt.steps.sort((a, b) => a.subtask_step_index - b.subtask_step_index);

                attempt.steps.forEach((item) => {
                    const itemDiv = document.createElement('div');
                    itemDiv.classList.add('collaboration-item'); // Generic class for all types of items

                    let headerText = '';
                    let itemContent = '';
                    let agentRoleClass = ''; // To apply specific styling based on agent type

                    if (item.type === 'subtask_message') {
                        itemDiv.classList.add('subtask-item');
                        headerText = `Subtask ${item.subtask_step_index + 1}: ${item.subtask_description}`;
                        itemContent = renderMessages(item.messages);
                        agentRoleClass = 'role-worker_node'; // Subtasks often involve worker nodes
                    } else if (item.type === 'task_planner_message') {
                        itemDiv.classList.add('planner-item');
                        headerText = `Task Planner (Step ${item.subtask_step_index + 1})`;
                        itemContent = renderMessages(item.messages, 'Task Planner');
                        agentRoleClass = 'role-task_planner';
                    } else if (item.type === 'coordinator_message') {
                        itemDiv.classList.add('coordinator-item');
                        headerText = `Coordinator (Step ${item.subtask_step_index + 1})`;
                        itemContent = renderMessages(item.messages, 'Coordinator');
                        agentRoleClass = 'role-coordinator';
                    } else {
                        // Fallback for unknown types
                        itemDiv.classList.add('unknown-item');
                        headerText = `Unknown Item (Step ${item.subtask_step_index + 1})`;
                        itemContent = JSON.stringify(item); // Show raw data for debugging
                    }

                    const itemHeader = document.createElement('h3');
                    itemHeader.textContent = headerText;
                    itemDiv.appendChild(itemHeader);
                    itemDiv.innerHTML += itemContent;
                    itemDiv.classList.add(agentRoleClass); // Apply the main agent role class to the whole item

                    attemptSection.appendChild(itemDiv);
                });
            } else {
                const noSteps = document.createElement('p');
                noSteps.textContent = 'No detailed steps found for this trajectory attempt.';
                attemptSection.appendChild(noSteps);
            }
            collaborationDetailsDiv.appendChild(attemptSection);
        });
    }

    function renderMessages(messages, defaultRolePrefix = '') {
        let messagesHtml = '';
        if (messages && messages.length > 0) {
            messages.forEach(message => {
                const role = message.role;
                const content = message.content;

                let roleClass = '';
                // Determine role class for specific styling
                if (role === 'user') {
                    roleClass = 'role-user';
                } else if (role === 'assistant') {
                    // Refined logic for assistant role based on general context or parsed content
                    if (content.includes("Assigned to Worker Node ID")) {
                        roleClass = 'role-coordinator';
                    } else if (content.includes("subtask:")) {
                         roleClass = 'role-task_planner';
                    } else if (defaultRolePrefix === 'Task Planner') { // If it's explicitly from planner history
                        roleClass = 'role-task_planner';
                    } else if (defaultRolePrefix === 'Coordinator') { // If it's explicitly from coordinator history
                        roleClass = 'role-coordinator';
                    } else if (content.includes("Tool Code Executed") || content.includes("Observation") || content.includes("Tool Output") || content.includes("Final Answer:")) {
                        roleClass = 'role-worker_node';
                    } else {
                        roleClass = 'role-assistant'; // Generic if not specialized
                    }
                }

                messagesHtml += `
                    <div class="message-box ${roleClass}">
                        <strong>${defaultRolePrefix ? defaultRolePrefix + ' ' : ''}${role}:</strong>
                        ${content.startsWith('{') && content.endsWith('}') ? `<pre>${content}</pre>` : `<span>${content.replace(/\n/g, '<br>')}</span>`}
                    </div>
                `;
            });
        } else {
            messagesHtml += '<p>No messages for this entry.</p>';
        }
        return messagesHtml;
    }

    fetchButton.addEventListener('click', () => {
        const selectedTaskId = taskSelect.value;
        if (selectedTaskId) {
            fetchCollaborationDetails(selectedTaskId);
        } else {
            mainTaskInfoDiv.innerHTML = '';
            collaborationDetailsDiv.innerHTML = '<p style="color: orange;">Please select a task ID first.</p>';
        }
    });

    populateTaskIds();
});