from abc import ABC, abstractmethod

from domain.ingestion.entities.document import Document


class DocumentRepository(ABC):

    @abstractmethod
    def save(self, document: Document) -> None:
        pass

    @abstractmethod
    def get(self, document_id: str) -> Document:
        pass

    @abstractmethod
    def delete(self, document_id: str) -> None:
        pass