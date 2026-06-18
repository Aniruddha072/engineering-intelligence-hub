from domain.ingestion.entities.document import Document
from domain.ingestion.ports.document_repository import DocumentRepository


class InMemoryDocumentRepository(DocumentRepository):

    def __init__(self):
        self.documents = {}

    def save(self, document: Document) -> None:
        self.documents[document.id] = document

    def get(self, document_id: str) -> Document:
        return self.documents[document_id]

    def delete(self, document_id: str) -> None:
        del self.documents[document_id]