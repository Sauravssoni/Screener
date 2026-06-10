# Redrob Ranker

deterministic and explainable ranking engine for the Redrob AI Track 1 challenge.

## Overview

This repository ranks candidate JSON files scoring profiles based on:
1. Core AI retrieval skills
2. Production shipping experience
3. Evaluation framework knowledge
4. Python and System architectures
5. Redrob behavioral metrics (activity, responses, location fit)

It avoids language model dependencies by using a rule-based weighted metric and deterministic parsers, ensuring execution under the 5-minute CPU constraint.

## Run Instructions

```bash
# Rank candidates
python rank.py --candidates candidates.jsonl --out submission.csv

# Validate the output
python validate_submission.py --candidates candidates.jsonl --submission submission.csv
```

## Running Tests
```bash
pytest
```
# Screener
