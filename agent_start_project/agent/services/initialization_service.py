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
        self.file_service = file_service
        self.tokenizer_service = tokenizer_service
        self.embedding_service = embedding_service
        self.tasklist_service = tasklist_service
        self.mcp_service = mcp_service
        self.rag_service = rag_service
