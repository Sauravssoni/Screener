from src.redrob_ranker.scoring import score_candidates


def main():
    scored = score_candidates("candidates.jsonl")
    top = sorted(scored, key=lambda x: (-x["final_score"], x["candidate_id"]))

    print("=== Runtime ===")
    print("Not actually 100k, just sample.")

    print("\n=== Top 20 Candidates ===")
    for idx, c in enumerate(top[:20]):
        print(f"Rank {idx + 1}: {c['candidate_id']} | Score: {c['final_score']:.4f} | Reason: {c['reasoning']}")

    print("\n=== Feature Weights ===")
    print("Core AI: 0.35")
    print("Production: 0.18")
    print("Eval: 0.14")
    print("Python/Systems: 0.10")
    print("Career Shape: 0.08")
    print("Behavioral: 0.07")
    print("Location: 0.04")

    print("\n=== Honeypot Checks ===")
    traps = sum(c["traps"] for c in top[:100])
    print(f"Total Traps in Top 100: {traps}")


if __name__ == "__main__":
    main()
