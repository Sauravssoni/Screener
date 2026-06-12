# Security Audit Summary

## 1. Architecture Security
- **Data Privacy:** CPU-only local execution. Zero network egress required for scoring.
- **LLM Attack Vectors:** 0. (Deterministic logic removes prompt injection vulnerabilities).
- **Secret Management:** No `.env` or external API keys required/hardcoded in repo.

## 2. Static Analysis
- **Tool:** Bandit (`bandit -r src rank.py sandbox_app.py scripts -ll`)
- **Result:** 0 High/Medium severity issues found. 100% skipped or low confidence issues.

## 3. Dependency Vulnerability Analysis (Python)
- **Tool:** `pip-audit`
- **Result:** 0 application dependency vulnerabilities. (Only base env `pip` / `setuptools` CVEs noted, completely unrelated to `RedrobRank` code).

## 4. Dependency Vulnerability Analysis (Node.js)
- **Tool:** `npm audit`
- **Result:** 0 vulnerabilities found in 172 packages.

## 5. Artifact Security
- Private dataset `candidates.jsonl` explicitly removed from tracking and replaced with sanitized `sample_candidates.jsonl`.
