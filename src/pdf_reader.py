"""PDF text extraction boundary."""
from io import BytesIO
from pypdf import PdfReader

def read_pdf(data: bytes) -> list[str]:
    if len(data) > 10 * 1024 * 1024 or not data.startswith(b"%PDF-"):
        raise ValueError("Select a text-based PDF under 10 MB.")
    try:
        reader = PdfReader(BytesIO(data))
        if reader.is_encrypted or not 1 <= len(reader.pages) <= 100:
            raise ValueError("Encrypted, empty, or over-100-page PDFs are not supported.")
        pages = [(page.extract_text() or "").strip() for page in reader.pages]
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError("Could not read the PDF.") from exc
    if sum(map(len, pages)) < 40:
        raise ValueError("No usable selectable text found; scanned PDFs require OCR.")
    return pages
