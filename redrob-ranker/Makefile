.PHONY: install lint format test coverage rank validate audit

install:
	pip3 install -r requirements.txt
	pip3 install -e ".[dev]"

lint:
	ruff check .

format:
	ruff format --check .

test:
	pytest

coverage:
	coverage run -m pytest
	coverage report

rank:
	python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv

validate:
	python3 validate_submission.py --candidates data/candidates.jsonl --submission submissions/submission.csv

audit:
	python3 scripts/audit_top_candidates.py --submission submissions/submission.csv
