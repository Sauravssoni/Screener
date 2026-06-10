# Weight Experiments

We iterated over multiple weight permutations using the `data/candidates.jsonl` target distribution.

## Variant 1: Core Heavy
* **Core** 0.50 | **Prod** 0.15 | **Eval** 0.10 | **Python** 0.10 | **Behav** 0.15
* *Result*: Pushed keyword stuffers slightly too high. Lack of robust honeypot penalties harmed top 10 reliability.

## Variant 2: Behavior Boosted
* **Core** 0.30 | **Prod** 0.20 | **Eval** 0.10 | **Python** 0.10 | **Behav** 0.30
* *Result*: Shuffled the top 10 with too much noise; product managers acting as ICs ranked up due to extremely high communication metrics. 

## Variant 3: Honeypot Strict & Evaluation Anchored (Chosen)
* **Core** 0.35 | **Prod** 0.18 | **Eval** 0.14 | **Python** 0.10 | **Behav** 0.07 | **Location** 0.04
* *Result*: Pristine Top 10. The 14% anchor on evaluation metrics effectively removed tutorial-only builders who hadn't mastered NDCG/A-B testing. Honeypot penalties (subtracted outright via traps counter) wiped spoofing candidates out of the top 50 permanently.
