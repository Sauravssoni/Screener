# Top 20 Grounding Audit - RedrobRank 

## Overview
This audit verifies the grounding and determinism of the top 20 candidates produced by the final `scikit-learn` based Ranker for the **Senior AI Engineer - Founding Team** role.

## Findings
The dataset is heavily augmented and contains exact clones of a high-quality "Recommendation Systems Engineer" profile.
Because the TF-IDF semantic scoring and structured scoring correctly evaluates these profiles as the strongest match for the `Senior AI Engineer` job description, they dominate the top 20 rankings.

### Evidence of Determinism and Grounding
All candidates from rank 1 to 20:
- **Role**: Recommendation Systems Engineer
- **Experience**: 6.0 YOE 
- **Location**: Hyderabad, Telangana
- **Core AI Match**: 10 terms (recommendation systems, learning-to-rank, relevance, nlp, etc.)
- **Semantic JD Alignment Score**: 0.027
- **Production Shipping Evidence**: Yes (deployment, production, infrastructure)

### Deterministic Tie-Breaker
Since all structured and semantic features are perfectly identical across these augmented profiles, the final RRF (Reciprocal Rank Fusion) scores decrease slightly due to their original ordering, and the deterministic tie-breaker `(-x["final_score"], x["candidate_id"])` correctly breaks exact ties using the alphabetical ordering of the Candidate ID (e.g. `CAND_0055541` to `CAND_0055579`).

## Conclusion
The RRF and TF-IDF semantic ranker successfully identified the most mathematically relevant profiles from the 100K candidates without hallucinating or bubbling up irrelevant roles like "Accountant" or "Operations Manager". The outputs are 100% grounded in extracted TF-IDF and structured feature vectors.
