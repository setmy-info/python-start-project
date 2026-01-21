# agent-start-project

FastAPI playground API with MCP metadata and a CLI AI agent that uses MCP and RAG to interact with it.

## Chosen platform

* **ChromaDV** as vector database
* **OpenAI** as example.

## Installation

```shell
source .venv/bin/activate
```

```shell
pip install -r requirements.txt
```

## Execution REST service

```shell
uvicorn api.main:app --reload --host 127.0.0.1 --port 5000
# Or with SMI tools
smi-venv-command uvicorn agent_start_project.api.main:app --reload --host 127.0.0.1 --port 5000
```

## Execution CLI Agent

Illustrating multiple rules folders and multiple MCP servers endpoints

```shell
export OPENAI_API_KEY=your_api_key_here
smi-venv-command python agent_start_project/agent/main.py --rules ./agent_start_project/rules ./agent_start_project/rules --mcp http://127.0.0.1:5000/mcp http://127.0.0.1:5000/mcp -t ./agent_start_project/tasks/example.md ./agent_start_project/tasks/example.md
```
