# RedrobRank Agentic Recruiter OS

“An offline, deterministic TalentOps ranking engine that converts 100,000 Redrob candidate profiles into a grounded Top-100 Senior AI Engineer shortlist.”

**Team ID:** Syntheon
**Team Name:** Syntheon
**Team Leader:** Saurav Soni
**Challenge:** Redrob / India.Runs Data & AI Challenge — Intelligent Candidate Discovery
**Output:** Top-100 candidate ranking CSV

---

## Evaluator Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv
python3 validate_submission.py submissions/submission.csv
python3 -m src.redrob_ranker.validation --candidates data/candidates.jsonl --submission submissions/submission.csv
python3 scripts/forensic_audit.py --csv submissions/submission.csv --jsonl data/candidates.jsonl --out reports/final_ranking_audit.md

npm install
npm run dev
streamlit run sandbox_app.py
```

*Note: Place the private challenge dataset at `data/candidates.jsonl`. The raw dataset is intentionally not committed to protect PII.*

---

## Why this beats generic rankers

* **Not keyword-only**: We parse structured YOE, titles, and semantic overlap, not just raw text matching.
* **Not API/LLM dependent**: LLMs hallucinate fit and cost thousands of dollars for 100K profiles. We run locally on CPU in seconds.
* **Deterministic and reproducible**: The exact same input always produces the exact same output.
* **Checks title/YOE/location grounding**: Firm guardrails drop unqualified profiles before semantic scoring.
* **Suppresses non-fit roles and keyword stuffing**: Generative honeypot penalties reduce the score of generic developers who sprinkle "AI" in their resumes.
* **Produces validator-safe CSV**: Built-in scripts guarantee the 5MB, 100-row format.
* **Local dashboard reads deterministic `/reports` artifacts**: Front-end works strictly offline.
* **Streamlit sandbox**: Lets evaluators test small samples without exposing the 100K dataset.

---

## Architecture

Candidate JSONL
→ Streaming loader
→ Evidence extraction
→ TF-IDF lexical recall
→ Structured fit scoring
→ Risk / honeypot penalties
→ RRF fusion
→ Grounded reasoning
→ CSV validator
→ Forensic audit
→ Dashboard / sandbox

---

## Ranking Signals

| Signal | What it captures | Why it matters |
|---|---|---|
| AI/retrieval/ranking/LLM evidence | Mentions of RAG, Transformers, PyTorch, etc. | Core JD requirement for AI Engineering. |
| Current title and career relevance | If the current role is an AI/ML/Data position | Ensures we aren't hiring a frontend engineer for a senior ML role. |
| Production/MLOps evidence | Deployment, scaling, CI/CD, Kubernetes | Differentiates seniors who deploy from juniors who just use Jupyter. |
| Evaluation/experimentation | A/B testing, metrics, robust evaluation | Critical for deploying models in real-world environments. |
| Python/systems/data infra | Python, Spark, databases, streaming | Foundational engineering skills. |
| Redrob behavioral availability | `is_available` flag | Don't recommend candidates who are not open to work. |
| Location/relocation | Current city vs JD location (Bangalore) | Checks geographic alignment or remote capacity. |
| Risk penalties | Honeypots, generic descriptions, low YOE | Filters out noise and inflated profiles. |

---

## Final Output Quality

* 100 ranked rows
* under 5MB
* 74 unique scores
* 100 unique reasonings
* 0 observed forensic hallucination/rule failures
* top 20 contains no obvious non-fit roles
* no raw dataset committed

---

## Top 10 Preview

| Rank | Candidate ID | Title | YOE | Location | Score | Why surfaced |
|---|---|---|---|---|---|---|
| 1 | CAND_0018499 | Senior ML Engineer | 7.2 | Noida, Uttar Pradesh | 0.0310 | Senior Machine Learning Engineer with 7.2 YOE based in Noida, Uttar Pradesh. Strong AI... |
| 2 | CAND_0005260 | Senior NLP Engineer | 5.2 | Chennai, Tamil Nadu | 0.0300 | Senior NLP Engineer with 5.2 YOE based in Chennai, Tamil Nadu. Strong AI indicators... |
| 3 | CAND_0046525 | Senior ML Engineer | 6.1 | Pune, Maharashtra | 0.0281 | Senior Machine Learning Engineer with 6.1 YOE based in Pune, Maharashtra. Strong... |
| 4 | CAND_0081846 | Lead AI Engineer | 6.7 | Jaipur, Rajasthan | 0.0267 | Lead AI Engineer with 6.7 YOE based in Jaipur, Rajasthan. Strong AI indicators... |
| 5 | CAND_0042506 | Search Engineer | 4.2 | Mumbai, Maharashtra | 0.0262 | Search Engineer with 4.2 YOE based in Mumbai, Maharashtra. Strong AI indicators... |
| 6 | CAND_0041669 | Recommendation Sys | 8.0 | Noida, Uttar Pradesh | 0.0253 | Recommendation Systems Engineer with 8.0 YOE based in Noida, Uttar Pradesh. Strong... |
| 7 | CAND_0007460 | AI Engineer | 4.7 | Pune, Maharashtra | 0.0247 | AI Engineer with 4.7 YOE based in Pune, Maharashtra. Strong AI indicators with... |
| 8 | CAND_0092278 | Senior NLP Engineer | 6.8 | Pune, Maharashtra | 0.0246 | Senior NLP Engineer with 6.8 YOE based in Pune, Maharashtra. Strong AI indicators... |
| 9 | CAND_0026532 | Recommendation Sys | 4.8 | Chennai, Tamil Nadu | 0.0233 | Recommendation Systems Engineer with 4.8 YOE based in Chennai, Tamil Nadu. Strong... |
| 10 | CAND_0086022 | Sr Applied Scientist| 5.3 | Kolkata, West Bengal | 0.0229 | Senior Applied Scientist with 5.3 YOE based in Kolkata, West Bengal. Strong AI i... |

---

## Dashboard / Sandbox

* React/Vite dashboard is a local report viewer
* no backend database needed
* reads deterministic JSON artifacts in `/reports`
* sandbox uses sanitized `sample_candidates.jsonl`
* sandbox is intentionally capped for small samples; full 100K runs via CLI

---

## Security & Privacy

* CPU-only execution
* no external LLM/API usage
* no secrets/API keys embedded
* no raw data committed to GitHub
* dashboard is local-only by default
* `npm run dev:network` only for intentional LAN demo
* Bandit/pip-audit/npm audit clean across local reports

---

## Limitations / Honest Notes

* No hidden labels were provided, so we do not claim artificial MAP/NDCG numbers against a hidden truth.
* Ranking is optimized strictly from structured profile evidence and JD signals.
* The forensic audit validates output grounding but does not replace final human review.
* A deterministic approach prioritizes absolute reproducibility and data privacy over opaque black-box semantic models.

---

## Submission Artifacts

| Artifact | Path/Link |
|---|---|
| GitHub Repo | [Sauravssoni/Screener](https://github.com/Sauravssoni/Screener) |
| Ranked CSV | [submissions/submission.csv](submissions/submission.csv) |
| Official Deck PDF | [docs/RedrobRank_Official_Submission_Deck.pdf](docs/RedrobRank_Official_Submission_Deck.pdf) |
| Approach Doc | [docs/APPROACH.md](docs/APPROACH.md) |
| Security Doc | [docs/SECURITY.md](docs/SECURITY.md) |
| Reproducibility Doc | [docs/REPRODUCIBILITY.md](docs/REPRODUCIBILITY.md) |
| Forensic Audit | [reports/final_ranking_audit.md](reports/final_ranking_audit.md) |

---

## Final Submission Verification

> **Note to Evaluators:** An automated GitHub Actions CI pipeline was originally configured for this repository to enforce strict quality, linting, and security (Bandit) checks on every push. However, due to a GitHub billing/account lock limiting GitHub Actions free-tier minutes on the primary account, the workflow runs were failing to start (yielding an instant "failure" state). As a result, the `.github/workflows` directory was removed from the final submission to maintain a clean repository. All validation (Ruff, PyTest, npm audit, Bandit, submission shape) passes 100% locally.

**Required Submission Paths for India.Runs Portal:**
1. **GitHub URL:** [https://github.com/Sauravssoni/Screener](https://github.com/Sauravssoni/Screener)
2. **Submission Output:** `submissions/submission.csv` (100 strictly-ranked candidates, <5MB)
3. **Official Pitch Deck:** `docs/RedrobRank_Official_Submission_Deck.pdf` (11 slides, containing exact Team ID: `Syntheon`)
