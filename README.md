# Materials Paper Summariser

A local, extractive overview of a **single text-based PDF** for materials research. It selects existing passages about synthesis, structure/characterisation and optical properties. It does not call an LLM, rewrite findings, or assess scientific validity. This is distinct from [RareEarthRAG](https://github.com/kalpanaiitm/RareEarthRAG), which searches across a collection.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Upload a permitted PDF under 10 MB and 100 pages. The app extracts selectable text in memory, selects matching passages and displays them for manual checking. Scans require OCR and are rejected. Keyword selection can miss relevant findings or pick a misleading sentence. Avoid confidential documents on hosted deployments.

## Test

`python -m pytest -q` covers passage selection and invalid PDF rejection. No scientific-accuracy benchmark has been completed. See `PROJECT_BLUEPRINT.md` and `TEST_REPORT.md` for scope and verification status.
