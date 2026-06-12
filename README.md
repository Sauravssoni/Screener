# RedrobRank Agentic Recruiter OS

**A deterministic, CPU-only, no-LLM candidate discovery engine for Redrob’s Intelligent Candidate Discovery challenge.**

![CPU-only](https://img.shields.io/badge/Architecture-CPU--only-blue)
![No external APIs](https://img.shields.io/badge/Network-No%20external%20APIs-success)
![No raw dataset committed](https://img.shields.io/badge/Security-No%20raw%20dataset%20committed-green)
![Validator compliant](https://img.shields.io/badge/Validation-Compliant-brightgreen)
![Forensic audit enabled](https://img.shields.io/badge/Audit-Forensic%20enabled-blueviolet)
![Local dashboard](https://img.shields.io/badge/UI-Local%20dashboard-orange)
![Sample sandbox](https://img.shields.io/badge/Demo-Sample%20sandbox-yellow)

## Final Deliverables

| Artifact | Path |
| :--- | :--- |
| **GitHub repo** | (This repository) |
| **Ranked CSV** | `submissions/submission.csv` |
| **Official Deck** | `docs/RedrobRank_Official_Submission_Deck.pdf` |
| **Methodology** | `docs/RedrobRank_Methodology.pdf` |
| **Audit Report** | `reports/final_ranking_audit.md` |
| **Sandbox App** | `sandbox_app.py` |

## Quickstart

```bash
pip install -r requirements.txt
python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv
python3 validate_submission.py submissions/submission.csv
python3 -m src.redrob_ranker.validation --candidates data/candidates.jsonl --submission submissions/submission.csv
python3 scripts/forensic_audit.py --csv submissions/submission.csv --jsonl data/candidates.jsonl --out reports/final_ranking_audit.md
npm install && npm run dev
streamlit run sandbox_app.py
```

## Architecture

`candidate JSONL` → `feature extraction` → `TF-IDF recall` → `structured scoring` → `risk filters` → `RRF fusion` → `grounded reasoning` → `CSV + reports` → `dashboard/sandbox`

## Scoring Methodology

* **AI/retrieval/ranking/LLM:** Lexical relevance for key NLP and ranking concepts.
* **production/MLOps:** Detects keywords proving the candidate ships to production (e.g., latency, kubernetes).
* **evaluation/experimentation:** Identifies metrics and A/B test methodologies (e.g., ndcg, mrr).
* **Python/systems:** Validates the underlying backend and data structures competence.
* **YOE fit:** Scores candidates strictly based on the 5-9 YOE sweet spot.
* **location/relocation:** Preferred locations and relocation flexibility.
* **behavioral signals:** Redrob response rates, GitHub activity, open-to-work flags.
* **risk penalties:** Harsh hard disqualifiers for title mismatches (manager-only, customer support) or missing constraints.

## Explainability

Reasoning uses the actual candidate title, YOE, location, matched skills, production/eval evidence, response signal, and candidate_id ref. There are **zero hallucinated justifications**.

### Top 10 Preview (from actual submission.csv)

1. **CAND_0018499**: Senior Machine Learning Engineer, 7.2 YOE, Noida
2. **CAND_0005260**: Senior NLP Engineer, 5.2 YOE, Chennai
3. **CAND_0046525**: Senior Machine Learning Engineer, 6.1 YOE, Pune
4. **CAND_0081846**: Lead AI Engineer, 6.7 YOE, Jaipur
5. **CAND_0042506**: Search Engineer, 4.2 YOE, Mumbai
6. **CAND_0041669**: Recommendation Systems Engineer, 8.0 YOE, Noida
7. **CAND_0007460**: AI Engineer, 4.7 YOE, Pune
8. **CAND_0092278**: Senior NLP Engineer, 6.8 YOE, Pune
9. **CAND_0026532**: Recommendation Systems Engineer, 4.8 YOE, Chennai
10. **CAND_0086022**: Senior Applied Scientist, 5.3 YOE, Kolkata

## Security

* **no external LLM/API calls:** Everything runs locally and securely.
* **no secrets:** No `.env` keys required.
* **no raw dataset:** The 100k line dataset is omitted; a mock 10-line sample is provided.
* **no browser full-dataset upload:** Safe data handling.
* **dashboard local report viewer only:** The frontend React dashboard only connects to local JSON.
* **sandbox limited sample upload only:** Streamlit sandbox is securely walled.

## Competitive Differentiation

* **not keyword-only:** Incorporates holistic signals beyond just regex matching.
* **not LLM-based:** 100% deterministic, fast, cheap, and immune to prompt injection.
* **no hallucinated justifications:** The forensic audit explicitly fails if a justification mismatches the candidate metadata.
* **not toy sample-only:** Designed to scale to 100k+ inputs seamlessly.
* **handles honeypots/role mismatches:** Filters out noise and false-positives directly via rigid logic.
* **deterministic tie-break and validator compliance:** Passes all Redrob compliance scripts explicitly.
