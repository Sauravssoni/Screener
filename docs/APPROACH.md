# Approach: Intelligent Candidate Discovery

## Challenge Framing
Redrob required ranking 100,000 candidate profiles to find the top 100 fits for a Senior AI Engineer role. We needed a solution that was robust, grounded, scalable, and completely free of LLM hallucinations.

## Ranking Signals
We extracted deterministic signals directly from profile JSON:
- **Lexical Relevance**: TF-IDF scoring of candidate current titles, skills, and past experience against the AI Engineer JD.
- **Structural Fit**: Years of Experience boundaries and hard role constraints.
- **Location/Availability**: Penalizing non-relocatable or unavailable candidates.
- **Risk Penalties**: Honeypots and non-AI generic engineering roles are down-weighted.

## Scoring & Fusion
Each candidate is scored across multiple signals. These scores are normalized and fused using a weighted Reciprocal Rank Fusion (RRF) approach to create a single stable metric.

## Reason Generation
Reasons are generated via template filling based on the raw extracted JSON features, guaranteeing 100% grounding. Zero observed forensic failures.

## Why Deterministic / No LLM?
Relying on external LLM APIs for 100K profiles is slow, expensive, and non-deterministic. A deterministic feature-based ranker ensures reproducibility, handles the large scale offline in seconds, and eliminates the risk of hallucinating skills a candidate doesn't have.

## Limitations
- No hidden labels provided, meaning MAP/NDCG cannot be claimed against a hidden truth.
- Ranking depends strictly on structured profile evidence; candidates with poor descriptions may score lower.
