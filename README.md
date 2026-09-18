# Materials Paper Search Assistant

A Streamlit application for searching a local collection of rare-earth materials research papers with transparent TF-IDF similarity matching.

> **Portfolio status:** working learning project. It retrieves relevant passages; it does not yet generate LLM answers or claim full RAG functionality.

## Why I built it

My PhD research focused on rare-earth materials chemistry. This project connects that domain knowledge with Python, scientific text processing and information retrieval—showing how specialist literature can be made easier to explore.

## What it does

- extracts text from PDFs stored locally
- builds a TF-IDF search index
- accepts natural-language research questions
- ranks relevant passages using cosine similarity
- displays source filenames and similarity scores
- runs without a paid API or external LLM

Example questions include:

- Which compounds show luminescence?
- What synthesis methods are discussed?
- Which papers mention powder XRD?
- Which rare-earth elements are present?

## Technical workflow

```text
Local PDFs → text extraction → text sections → TF-IDF index
                                           ↓
Research question → query cleaning → cosine similarity → ranked passages
```

## Tech stack

Python · Streamlit · scikit-learn · PDF text extraction · TF-IDF · cosine similarity

## Run locally

```bash
git clone https://github.com/kalpanaiitm/MaterialsPaperSummariser.git
cd MaterialsPaperSummariser
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Add papers that you are permitted to use to `data/papers/`. Do not commit copyrighted or confidential papers.

## Current limitations

- works with text-based PDFs; scanned documents require OCR
- retrieval quality depends on PDF extraction and wording overlap
- returns relevant passages rather than generated answers
- has not yet been evaluated on a benchmark dataset

## Next steps

- add sentence-transformer embeddings and compare them with TF-IDF
- add citation-aware answer generation
- create an evaluation set for retrieval quality
- extract compounds, synthesis conditions and characterisation methods
- add automated tests and a hosted demonstration

## About the builder

Created by Dr Kalpana Govindarasan, a materials chemist transitioning into applied AI and building practical tools at the intersection of scientific knowledge, retrieval and responsible AI.
