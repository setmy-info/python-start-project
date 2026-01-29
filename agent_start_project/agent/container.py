import argparse

from tokenizer_service import TokenizerService
from cli import CLIParser
from embedding_service import EmbeddingService
from file_service import FileService
from tasklist_service import TasklistService
from mcp_service import McpService
from rag_service import RagService
from initialization_service import InitializationService

cli_parser = CLIParser(argparse.ArgumentParser(description="AI Agent CLI"))
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
