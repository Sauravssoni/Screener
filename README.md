# RedrobRank Agentic Recruiter OS

RedrobRank is a 10-stage deterministic scoring engine designed to efficiently process and rank candidates for the Senior AI Engineer role at Redrob AI. It features a robust Lexical TF-IDF module, Reciprocal Rank Fusion (RRF), and hard disqualifiers to ensure complete factual grounding without hallucination.

## Final Deliverables

* `submissions/submission.csv`
* `docs/RedrobRank_Methodology.pdf`

*Note: The raw dataset is not included in this repository to protect privacy and comply with competition security standards.*

## How to run

```bash
python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv
```

## How to validate

```bash
python3 validate_submission.py submissions/submission.csv
python3 -m src.redrob_ranker.validation --candidates data/candidates.jsonl --submission submissions/submission.csv
```

## How to run dashboard

```bash
npm install
npm run dev
```

## Security

* **CPU-only:** The engine operates securely without the need for GPU acceleration.
* **No external LLM/API calls:** Ensures zero data leakage and deterministic performance.
* **No secrets:** The codebase contains no hidden API keys or passwords.
* **No raw dataset committed:** Only a tiny sample dataset is included.
* **Dashboard is static/local:** The RecruiterOps dashboard is purely a local report viewer.
