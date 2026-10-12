
from pathlib import Path
import pymupdf
from docx import Document

def read_document(file_path):
    path = Path(file_path)
    extension = path.suffix.lower()

    try:
        if extension == ".txt":
            return path.read_text(encoding="utf-8")

        elif extension == ".pdf":
            with pymupdf.open(path) as pdf:
                return "\n".join(
                    page.get_text() for page in pdf
                )

        elif extension == ".docx":
            doc = Document(path)
            return "\n".join(
                paragraph.text
                for paragraph in doc.paragraphs
            )

        else:
            return "Unsupported file type."

    except Exception as error:
        return f"Could not read document: {error}"
