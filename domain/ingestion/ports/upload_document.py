from domain.ingestion.ports.document_repository import DocumentRepository
from domain.ingestion.ports.file_storage import FileStorage


class UploadDocument:

    def __init__(
        self,
        document_repository: DocumentRepository,
        file_storage: FileStorage,
    ):
        self.document_repository = document_repository
        self.file_storage = file_storage