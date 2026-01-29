from file_service import FileService
from tokenizer_service import TokenizerService
from embedding_service import EmbeddingService
from tasklist_service import TasklistService
from mcp_service import McpService
from rag_service import RagService


class InitializationService:

    def __init__(self, file_service: FileService, tokenizer_service: TokenizerService,
                 embedding_service: EmbeddingService, tasklist_service: TasklistService, mcp_service: McpService,
                 rag_service: RagService):
        pass
