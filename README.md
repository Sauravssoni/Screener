# RedrobRank Agentic Recruiter OS

A deterministic and explainable ranking engine for the Redrob AI Track 1 candidate ranking challenge.

## Overview
This repository ranks candidate profiles based on core AI retrieval skills, production shipping experience, evaluation framework knowledge, Python architectures, and behavioral metrics. 

**Synthetic Cluster Note:** The benchmark contains repeated high-fit candidate templates, so top candidates may share identical score/reasoning; deterministic `candidate_id` tie-break is used.

## Final Deliverables
* `submissions/submission.csv` (The ranked output of exactly 100 candidates)
* `docs/RedrobRank_Methodology.pdf` (The methodology and system architecture report)

*Note: No raw dataset is included in this repository to protect data privacy.*

## Security & Architecture
* **CPU-only:** Executes fully locally.
* **No external LLM/API calls:** Secure and offline.
* **No secrets/API keys:** None required or tracked.
* **No raw dataset committed:** Protected information remains strictly local.
* **Static Dashboard:** The dashboard is a static/local report viewer only and exposes no backend API. (Express is used strictly by Vite dev middleware for local preview of generated JSONs).

## Run Instructions

### Rank Candidates
```bash
python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv
```

### Validate Submission
```bash
python3 validate_submission.py submissions/submission.csv
python3 -m src.redrob_ranker.validation --candidates data/candidates.jsonl --submission submissions/submission.csv
```

### Run Local Dashboard Viewer
```bash
npm install
npm run dev
```

## Running Tests
```bash
pytest
```
