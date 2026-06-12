# Security & Privacy

This repository prioritizes data security and evaluator safety.

## No Raw Dataset Committed
The `data/candidates.jsonl` containing 100,000 profiles is in `.gitignore` and never leaves the host machine.

## No Secrets
We use no external APIs. There are no exposed API keys.

## CPU-Only & Offline
The ranking engine runs entirely on local CPU and memory without dialing home to external AI models.

## Local Dashboard
The included React dashboard is strictly local. It reads static JSON artifacts generated in the `reports/` folder.
A `sandbox_app.py` script ensures safe local testing with sample data.

## Audit Tools
We rely on `bandit`, `npm audit`, and `ruff` to ensure there are no unintended injection risks or loose code.
