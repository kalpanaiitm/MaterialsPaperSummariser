from src.summariser import summarise_text
from src.pdf_reader import read_pdf
import pytest

def test_extracts_only_existing_passages():
    result = summarise_text("The material was prepared at room temperature. Powder XRD confirmed crystallinity.")
    assert "prepared" in result["Synthesis"]
    assert "XRD" in result["Structure and characterisation"]
    assert result["Optical properties"] == ""

def test_rejects_non_pdf():
    with pytest.raises(ValueError):
        read_pdf(b"not a PDF")
