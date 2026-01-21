import os

import openai

from container import cli_parser
from mcp import load_mcp
from model import ask_ai_to_process_tasks, execute_ai_tasks
from rules import load_rules
from tasks import load_tasklists


def main():
    args = cli_parser.parse_args()
    task_rules = load_rules(args.rules)

    print(f"Loaded {len(task_rules)} RULE files")
    for i, rule in enumerate(task_rules, start=1):
        print(f"\n--- File {i} ---")
        print(rule)
        print("--------------")

    all_mcp = []
    for url in args.mcp:
        mcp_json = load_mcp(url)
        if mcp_json:
            all_mcp.append(mcp_json)

    print("\nMCP endpoints:")
    for i, mcp in enumerate(all_mcp, start=1):
        print(f"\n--- MCP Server {i}: {mcp.get('serviceName')} ---")
        for ep in mcp.get("endpoints", []):
            print(f"  {ep['method']} {ep['path']} - {ep['description']}")

    tasklist_content = load_tasklists(args.tasklist)
    if not tasklist_content:
        print("Tasklist file cant be read.")
        return

    print("\nCombined Tasklist content:")
    print(tasklist_content)

    openai.api_key = os.getenv("OPENAI_API_KEY")
    ai_output = ask_ai_to_process_tasks(tasklist_content, task_rules, all_mcp)

    print("\nAI Model Output:")
    print(ai_output)

    execute_ai_tasks(ai_output, all_mcp)


if __name__ == "__main__":
    main()
