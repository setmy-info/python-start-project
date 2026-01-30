from agent_start_project.agent.services.tokenizer_service import TokenizerService
from agent_start_project.agent.services.embedding_service import EmbeddingService
from agent_start_project.agent.services.file_service import FileService
from agent_start_project.agent.services.tasklist_service import TasklistService
from agent_start_project.agent.services.mcp_service import McpService
from agent_start_project.agent.services.rag_service import RagService
from agent_start_project.agent.services.initialization_service import InitializationService

file_service = FileService()
tokenizer_service = TokenizerService()
embedding_service = EmbeddingService()
tasklist_service = TasklistService()
mcp_service = McpService()
rag_service = RagService()
initialization_service = InitializationService(
    file_service,
    tokenizer_service,
    embedding_service,
    tasklist_service,
    mcp_service,
    rag_service
)
