from dataclasses import dataclass
from enum import Enum
from datetime import datetime


class DocumentStatus(Enum):
    UPLOADED = "uploaded"
    PROCESSING = "processing"
    INDEXED = "indexed"
    FAILED = "failed"


@dataclass
class Document:
    id: str
    filename: str
    content_type: str
    file_size: int
    status: DocumentStatus
    created_at: datetime
    updated_at: datetime
    