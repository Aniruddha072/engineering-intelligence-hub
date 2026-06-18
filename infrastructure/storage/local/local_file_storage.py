from pathlib import Path

from domain.ingestion.ports.file_storage import FileStorage


class LocalFileStorage(FileStorage):

    def __init__(self, upload_directory: str):
        self.upload_directory = Path(upload_directory)
        self.upload_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(
        self,
        filename: str,
        content: bytes
    ) -> str:

        file_path = self.upload_directory / filename

        with open(file_path, "wb") as file:
            file.write(content)

        return str(file_path)