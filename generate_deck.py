from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_deck():
    c = canvas.Canvas("docs/RedrobRank_Official_Submission_Deck.pdf", pagesize=landscape(letter))
    width, height = landscape(letter)

    def draw_slide(title, body_lines):
        c.setFillColor(colors.darkblue)
        c.rect(0, 0, width, height, fill=1)
        
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(40, height - 60, title)
        
        c.setStrokeColor(colors.white)
        c.line(40, height - 70, width - 40, height - 70)
        
        c.setFont("Helvetica", 14)
        y = height - 100
        for line in body_lines:
            if line.startswith("- "):
                c.drawString(60, y, line)
            elif line.startswith("  * "):
                c.drawString(80, y, line)
            elif line.startswith("* "):
                c.drawString(60, y, line)
            else:
                c.drawString(40, y, line)
            y -= 25
        
        c.showPage()

    slides = [
        ("Slide 1: Title", [
            "Team Name: Syntheon",
            "Team Leader Name: Saurav Soni",
            "Problem Statement: Data & AI Challenge — Intelligent Candidate Discovery",
            "Solution: RedrobRank Agentic Recruiter OS"
        ]),
        ("Slide 2: Solution Overview", [
            "RedrobRank is a deterministic CPU-only TalentOps agent that ranks 100K candidates",
            "into a validator-compliant Top-100 shortlist.",
            "",
            "Differentiators:",
            "- JD-aware evidence extraction",
            "- production/evaluation/retrieval-first scoring",
            "- Redrob behavioral signal modulation",
            "- honeypot/risk filtering",
            "- no LLM/API calls",
            "- fully reproducible"
        ]),
        ("Slide 3: JD Understanding & Candidate Evaluation", [
            "JD requirements:",
            "- 5–9 YOE senior AI engineer",
            "- retrieval/ranking/LLM/fine-tuning",
            "- production shipping",
            "- evaluation infrastructure",
            "- recruiter/product workflow mindset",
            "- Pune/Noida/tier-1 India/relocation",
            "",
            "Signals: title + career history, actual skills, production terms, evaluation terms,",
            "         Redrob signals, risk flags",
            "Beyond keyword matching: penalizes non-technical roles, checks production depth,",
            "                         checks evaluation language, acknowledges concerns"
        ]),
        ("Slide 4: Ranking Methodology", [
            "Pipeline:",
            "1. Stream JSONL",
            "2. Extract text from profile/career/skills/signals",
            "3. Score by weighted evidence",
            "4. Apply risk penalties",
            "5. Sort score desc + candidate_id tie-break",
            "6. Generate grounded reasoning",
            "",
            "Weights:",
            "AI/retrieval/ranking, production, evaluation, systems, YOE,",
            "location, behavioral signals, risk."
        ]),
        ("Slide 5: Explainability & Data Validation", [
            "Each reasoning references:",
            "- actual title",
            "- YOE",
            "- location",
            "- matched skills",
            "- production/eval count",
            "- Redrob response/open/relocation signal",
            "",
            "Hallucination prevention: no LLM generation, only deterministic extracted evidence,",
            "                          validator + grounding audit",
            "Suspicious profiles: honeypot penalties, role mismatch penalties,",
            "                     pure research / manager-only checks"
        ]),
        ("Slide 6: End-to-End Workflow", [
            "JD -> Signal Dictionary",
            "      -> Candidate JSONL Stream",
            "         -> Feature Extractor",
            "            -> Risk Detector",
            "               -> Weighted Ranker",
            "                  -> Top-100 CSV",
            "                     -> Validator",
            "                        -> Dashboard/Sandbox"
        ]),
        ("Slide 7: System Architecture", [
            "CLI Ranker:",
            "- JD config, Candidate stream reader, Feature extractor, Scoring engine",
            "- Risk engine, Reasoning generator, CSV writer, report generator",
            "",
            "React Dashboard: reads reports/*.json",
            "Streamlit Sandbox: sample upload, sample rank, CSV download",
            "",
            "No network / no LLM / no GPU"
        ]),
        ("Slide 8: Results & Performance", [
            "- 100,000 candidates processed",
            "- runtime under 5 minutes CPU-only",
            "- final CSV validates",
            "- 100 ranked rows",
            "- no raw dataset committed",
            "- no external APIs",
            "- top-100 reasoning generated",
            "- trap/honeypot logic included"
        ]),
        ("Slide 9: Technologies Used", [
            "- Python",
            "- deterministic JSONL streaming",
            "- custom rule-based scoring",
            "- pytest / coverage / ruff",
            "- Bandit / Semgrep / pip-audit / npm audit",
            "- React + Vite dashboard",
            "- Streamlit sandbox",
            "- Sentrux structural quality scan",
            "- GitHub public repo"
        ]),
        ("Slide 10: Submission Assets", [
            "GitHub: https://github.com/Sauravssoni/Screener",
            "CSV: submissions/submission.csv",
            "Deck: docs/RedrobRank_Official_Submission_Deck.pdf",
            "Methodology: docs/RedrobRank_Methodology.pdf",
            "",
            "Run: python3 rank.py --candidates data/candidates.jsonl --out submissions/submission.csv",
            "Validate: python3 validate_submission.py submissions/submission.csv",
            "Sandbox: streamlit run sandbox_app.py"
        ]),
        ("Slide 11: Thank You", [
            "Thank You"
        ])
    ]

    for title, body in slides:
        draw_slide(title, body)

    c.save()

if __name__ == "__main__":
    create_deck()
