"""Local, extractive paper overview; no LLM or network service is used."""
import streamlit as st
from src.pdf_reader import read_pdf
from src.summariser import summarise_text

st.set_page_config(page_title="Materials Paper Summariser", layout="wide")
st.title("Materials Paper Summariser")
st.caption("Extractive overview of a text-based materials paper. Verify every passage against the PDF.")
uploaded = st.file_uploader("Select a PDF you have permission to process", type="pdf")
if uploaded:
    try:
        pages = read_pdf(uploaded.getvalue())
        overview = summarise_text("\n".join(pages))
    except ValueError as exc:
        st.error(str(exc))
    else:
        st.write(f"Pages: {len(pages)}")
        for label, passage in overview.items():
            st.subheader(label)
            st.write(passage or "No matching passage detected; review the paper manually.")
        st.info("This is keyword-based extraction, not a scientific assessment or a generated summary.")
