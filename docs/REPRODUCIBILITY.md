# Reproducibility Guide

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Ranker
```bash
# Ensure data/candidates.jsonl exists first
python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv
```

## Validating Output
```bash
python3 validate_submission.py submissions/submission.csv
```

## Forensic Audit
```bash
python3 scripts/forensic_audit.py --csv submissions/submission.csv --jsonl data/candidates.jsonl --out reports/final_ranking_audit.md
```

## Dashboard / Sandbox
```bash
npm install
npm run dev
# OR for streamlit:
streamlit run sandbox_app.py
```
