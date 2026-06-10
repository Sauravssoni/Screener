# Methodology: RedrobRank

## Architecture
The ranker processes `candidates.jsonl` using a deterministic, rule-based feature extractor and a highly calibrated weighting algorithm.

- **Extraction**: Streams JSONL, extracting text from profile headlines, summaries, and career histories.
- **Scoring**: Applies pre-defined keyword lists targeting:
  - Core AI & Retrieval
  - Production deployments (MLOps, scaling)
  - Evaluation (NDCG, MAP, A/B testing)
  - Python/Systems infrastructure.
- **Honeypot/Trap Detection**: Disqualifies candidates claiming "expert" status with minimal time experience, or keyword stuffers lacking evidence of production deployment.
- **Redrob Behavioral Signals**: Modulates baseline technical score relying upon profile activity and location matches.
