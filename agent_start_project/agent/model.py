import json

import requests


# from chromadb import Client
# from chromadb.config import Settings

def ask_ai_to_process_tasks(tasklist_content, task_rules, mcp_json_list):
    """
    Request AI
    """
    prompt = f"""
TASK rules:
{'\n'.join(task_rules)}

MCP metadata:
"""
    for mcp in mcp_json_list:
        prompt += f"\nService: {mcp.get('serviceName')}, endpoints:\n"
        for ep in mcp.get("endpoints", []):
            prompt += f"  {ep['method']} {ep['path']} - {ep['description']}\n"

    prompt += f"\n{tasklist_content}\n\n"

    # response = openai.ChatCompletion.create(
    #     model="gpt-4o-mini",
    #     messages=[
    #         {"role": "system", "content": "Sa oled AI agent, kes täidab taskliste MCP teenuste abil."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0
    # )
    # return response.choices[0].message.content
    return prompt


def execute_ai_tasks(ai_output, mcp_servers):
    try:
        tasks = json.loads(ai_output)
    except json.JSONDecodeError:
        print("AI output ei ole korrektne JSON.")
        print(ai_output)
        return

    for task in tasks:
        service_name = task.get("serviceName")
        endpoint_template = task.get("endpoint")
        method = task.get("method", "POST").upper()
        data = task.get("data", {})

        server_url = None
        for mcp in mcp_servers:
            if mcp.get("serviceName") == service_name:
                server_url = mcp.get("_url", None)
                break

        if not server_url:
            print(f"Server for {service_name} not found. Skipping task: {task}")
            continue

        if "{person_id}" in endpoint_template:
            person_id = len(data.get("firstName", "")) + len(data.get("lastName", ""))  # lihtne dummy ID
            endpoint = endpoint_template.replace("{person_id}", str(person_id))
        else:
            endpoint = endpoint_template

        url = f"{server_url}{endpoint}"

        try:
            if method == "POST":
                resp = requests.post(url, json=data)
            elif method == "GET":
                resp = requests.get(url, params=data)
            else:
                print(f"Method {method} not supported. Skipping.")
                continue

            if resp.status_code in (200, 201):
                print(f"[SUCCESS] {method} {url} -> {resp.json()}")
            else:
                print(f"[FAIL] {method} {url} -> {resp.status_code}: {resp.text}")

        except requests.RequestException as e:
            print(f"[ERROR] {method} {url} -> {e}")
