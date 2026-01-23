# agent-start-project

FastAPI playground API with MCP metadata and a CLI AI agent that uses MCP and RAG to interact with it.

## Chosen platform

* **ChromaDV** as vector database
* **OpenAI** as an example.

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

smi-venv-command python agent_start_project/agent/probe.py
```

    docker pull pgvector/pgvector:pg16

    docker run -d --name pgvector -p 5432:5432 -e POSTGRES_USER=rag -e POSTGRES_PASSWORD=rag -e POSTGRES_DB=ragdb pgvector/pgvector:pg16 docker exec -it pgvector psql -U rag -d ragdb

    CREATE EXTENSION vector;

    CREATE TABLE documents (
        id UUID PRIMARY KEY,
        source TEXT,
        content TEXT,
        embedding VECTOR(1536)  -- text-embedding-3-small
    );

    CREATE INDEX documents_embedding_idx
    ON documents
    USING ivfflat (embedding vector_cosine_ops)
    WITH (lists = 100);

    pip install psycopg[binary] pgvector

https://platform.openai.com/docs/guides/structured-outputs

https://platform.openai.com/docs/overview

https://platform.openai.com/usage

https://platform.openai.com/api-keys
