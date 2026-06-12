# RedrobRank Agentic Recruiter OS

Deterministic, CPU-only, no-LLM candidate discovery engine for the Redrob Data & AI Challenge: Intelligent Candidate Discovery.

![CPU-only](https://img.shields.io/badge/Architecture-CPU--only-blue) | ![No external APIs](https://img.shields.io/badge/Network-No%20external%20APIs-success) | ![No raw dataset committed](https://img.shields.io/badge/Security-No%20raw%20dataset%20committed-green) | ![Validator compliant](https://img.shields.io/badge/Validation-Compliant-brightgreen) | ![Forensic audit enabled](https://img.shields.io/badge/Audit-Forensic%20enabled-blueviolet) | ![Local dashboard](https://img.shields.io/badge/UI-Local%20dashboard-orange) | ![Streamlit sandbox](https://img.shields.io/badge/Demo-Streamlit%20sandbox-yellow)

## Final Submission Artifacts

| Artifact                     | Path                                         |
| ---------------------------- | -------------------------------------------- |
| Ranked CSV                   | `submissions/submission.csv`                   |
| Official deck PDF            | `docs/RedrobRank_Official_Submission_Deck.pdf` |
| Supplemental methodology PDF | `docs/RedrobRank_Methodology.pdf`              |
| Forensic audit report        | `reports/final_ranking_audit.md`               |
| Security audit summary       | `reports/security_audit_summary.md`            |
| Quality audit summary        | `reports/final_quality_audit.md`               |
| Local dashboard              | `src/` + `npm run dev`                           |
| Sample sandbox               | `sandbox_app.py` + `sample_candidates.jsonl`     |

## Why RedrobRank is different

* **Not keyword-only**: Uses semantic TF-IDF weights and multi-stage filtering.
* **Not LLM/API-based**: Avoids slow, expensive, and unpredictable black-box LLM calls.
* **Deterministic and reproducible**: The same input always produces the exact same output.
* **Grounded explanations only**: Zero hallucination risk. Every reason is strictly traceable to actual data.
* **Hard penalties for non-fit roles**: Aggressively filters out honeypots, generic managers, and customer support.
* **Forensic audit prevents title/YOE/location hallucinations**: A custom script fails CI if justifications lie.
* **CPU-only and data-private**: Fully local execution ensures enterprise data security.

## Architecture

```text
candidate JSONL
→ stream reader
→ feature extraction
→ TF-IDF lexical recall
→ structured scoring
→ risk filters
→ RRF fusion
→ grounded reasoning
→ validator-safe CSV
→ reports/dashboard/sandbox
```

## Scoring Methodology

* **AI/retrieval/ranking/LLM evidence**: Strongest weight for semantic search, vector databases, and RAG.
* **Skill trust**: Verification of listed skills against actual profile summaries.
* **Career relevance**: Prioritizes titles explicitly matching Senior AI/ML roles.
* **Production/MLOps**: Rewards keywords proving the candidate ships at scale (Kubernetes, latency, deployment).
* **Evaluation/experimentation**: Rewards knowledge of ML metrics (NDCG, MRR, A/B testing).
* **Behavioral availability**: Factors in GitHub activity, open-to-work flags, and Redrob response rates.
* **Location/relocation**: Adjusts scores based on preferred geographies.
* **Risk/honeypot penalties**: Disqualifies candidates with <3 YOE, irrelevant titles, or keyword stuffing.

## Top 10 Preview

1. CAND_0018499 — Senior Machine Learning Engineer — 7.2 YOE — Noida — score 0.0310
2. CAND_0005260 — Senior NLP Engineer — 5.2 YOE — Chennai — score 0.0300
3. CAND_0046525 — Senior Machine Learning Engineer — 6.1 YOE — Pune — score 0.0281
4. CAND_0081846 — Lead AI Engineer — 6.7 YOE — Jaipur — score 0.0267
5. CAND_0042506 — Search Engineer — 4.2 YOE — Mumbai — score 0.0262
6. CAND_0041669 — Recommendation Systems Engineer — 8.0 YOE — Noida — score 0.0253
7. CAND_0007460 — AI Engineer — 4.7 YOE — Pune — score 0.0247
8. CAND_0092278 — Senior NLP Engineer — 6.8 YOE — Pune — score 0.0246
9. CAND_0026532 — Recommendation Systems Engineer — 4.8 YOE — Chennai — score 0.0233
10. CAND_0086022 — Senior Applied Scientist — 5.3 YOE — Kolkata — score 0.0229

## Quickstart

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

## Security / Privacy

* No raw candidate dataset in GitHub
* No external LLM/API calls
* No secrets
* Local CPU-only processing
* Dashboard is static/local report viewer
* Sandbox is limited sample upload only

## Audit Results

* **Unique scores:** 74
* **Unique reasonings:** 100
* **Hallucination/rule failures:** 0
* **Quality report path:** `reports/final_quality_audit.md`
* **Security report path:** `reports/security_audit_summary.md`
