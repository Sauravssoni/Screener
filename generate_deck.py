import os
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def create_deck():
    os.makedirs("docs", exist_ok=True)
    c = canvas.Canvas("docs/RedrobRank_Official_Submission_Deck.pdf", pagesize=landscape(letter))
    width, height = landscape(letter)

    # Theme colors
    bg_color = colors.HexColor("#F8F9FA")
    text_color = colors.HexColor("#212529")
    accent_color = colors.HexColor("#D32F2F") # Redrob red
    secondary_accent = colors.HexColor("#673AB7") # Purple
    card_bg = colors.HexColor("#FFFFFF")
    light_text = colors.HexColor("#6C757D")

    def draw_bg():
        c.setFillColor(bg_color)
        c.rect(0, 0, width, height, fill=1, stroke=0)
        # Top banner
        c.setFillColor(accent_color)
        c.rect(0, height - 10, width, 10, fill=1, stroke=0)

    def draw_title(title):
        c.setFillColor(text_color)
        c.setFont("Helvetica-Bold", 32)
        c.drawString(50, height - 70, title)
        c.setStrokeColor(secondary_accent)
        c.setLineWidth(3)
        c.line(50, height - 85, 150, height - 85)

    def draw_card(x, y, w, h, title, lines, title_color=text_color):
        c.setFillColor(card_bg)
        c.setStrokeColor(colors.HexColor("#DEE2E6"))
        c.setLineWidth(1)
        c.roundRect(x, y, w, h, 8, fill=1, stroke=1)
        
        # Shadow effect
        c.setFillColor(colors.black)
        c.setStrokeColor(colors.black)
        # c.roundRect(x+2, y-2, w, h, 8, fill=1, stroke=0) # skip shadow for clean flat design
        
        c.setFillColor(title_color)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x + 15, y + h - 25, title)
        
        c.setFillColor(text_color)
        c.setFont("Helvetica", 14)
        curr_y = y + h - 50
        for line in lines:
            if line.startswith("- "):
                c.drawString(x + 25, curr_y, line)
            elif line.startswith("  * "):
                c.drawString(x + 40, curr_y, line)
            elif line.startswith("* "):
                c.drawString(x + 25, curr_y, line)
            else:
                c.drawString(x + 15, curr_y, line)
            curr_y -= 22

    def draw_metric_strip(labels):
        strip_y = 30
        c.setFillColor(secondary_accent)
        c.rect(0, strip_y, width, 40, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 14)
        
        segment = width / len(labels)
        for i, label in enumerate(labels):
            c.drawCentredString((i + 0.5) * segment, strip_y + 15, label)

    # SLIDE 1
    draw_bg()
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", 44)
    c.drawCentredString(width/2, height/2 + 50, "RedrobRank Agentic Recruiter OS")
    
    c.setFillColor(light_text)
    c.setFont("Helvetica", 20)
    c.drawCentredString(width/2, height/2 + 10, "Deterministic, CPU-only candidate discovery for the Redrob Data & AI Challenge")
    
    c.setFillColor(accent_color)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height/2 - 50, "Team Name: Syntheon")
    c.setFillColor(text_color)
    c.setFont("Helvetica", 16)
    c.drawCentredString(width/2, height/2 - 75, "Team Leader: Saurav Soni")
    c.drawCentredString(width/2, height/2 - 100, "Problem Statement: Intelligent Candidate Discovery")
    
    c.setStrokeColor(secondary_accent)
    c.setLineWidth(4)
    c.line(width/2 - 100, height/2 - 130, width/2 + 100, height/2 - 130)
    c.showPage()

    # SLIDE 2
    draw_bg()
    draw_title("Hiring AI talent from 100K profiles is not a keyword search problem")
    
    w = (width - 150) / 2
    draw_card(50, height - 300, w, 150, "1. Keyword stuffing", [
        "Candidates can list AI buzzwords",
        "without real depth."
    ])
    draw_card(50 + w + 50, height - 300, w, 150, "2. Ghost candidates", [
        "Strong profiles can be inactive,",
        "unavailable, or low-response."
    ])
    draw_card(50, height - 480, w, 150, "3. Domain mismatches", [
        "Support, accounting, civil/mechanical,",
        "HR, and content roles may contain AI keywords."
    ])
    draw_card(50 + w + 50, height - 480, w, 150, "4. Hallucinated explanations", [
        "Ranking systems fail trust if the reason",
        "does not match candidate facts."
    ])
    
    c.setFillColor(secondary_accent)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 60, "RedrobRank was built to optimize relevance + trust + reproducibility.")
    c.showPage()

    # SLIDE 3
    draw_bg()
    draw_title("RedrobRank turns 100K candidates into a grounded Top-100 shortlist")
    
    w = (width - 200) / 4
    draw_card(40, height - 350, w, 220, "1. Extract evidence", [
        "Title, YOE, location,",
        "career, skills, Redrob",
        "behavioral signals."
    ])
    draw_card(40 + w + 40, height - 350, w, 220, "2. Score fit", [
        "AI/retrieval, production,",
        "evaluation, systems,",
        "YOE, location, behavior."
    ])
    draw_card(40 + w*2 + 80, height - 350, w, 220, "3. Filter risk", [
        "Honeypots, keyword",
        "stuffers, non-fit roles,",
        "manager-only, low-signal."
    ])
    draw_card(40 + w*3 + 120, height - 350, w, 220, "4. Explain output", [
        "Every reason references",
        "actual candidate facts."
    ])
    
    draw_metric_strip(["100K processed", "100 final rows", "CPU-only", "No LLM/API", "Validator passed"])
    c.showPage()

    # SLIDE 4
    draw_bg()
    draw_title("What the Senior AI Engineer JD actually needs")
    
    w = (width - 150) / 2
    draw_card(50, height - 450, w, 300, "Must-have signals", [
        "- Retrieval / vector search / semantic search",
        "- Ranking / recommender systems / personalization",
        "- LLM / RAG / fine-tuning / NLP",
        "- Production ML / MLOps / deployment",
        "- Evaluation: NDCG, MRR, A/B testing",
        "- Python + systems/data infrastructure"
    ], title_color=colors.HexColor("#2E7D32")) # Green
    
    draw_card(50 + w + 50, height - 450, w, 300, "Negative signals", [
        "- Non-technical role mismatch",
        "- Prompt-only or keyword-stuffed profiles",
        "- Pure management without recent technical depth",
        "- Pure research without production evidence",
        "- Weak availability/engagement"
    ], title_color=accent_color)
    c.showPage()

    # SLIDE 5
    draw_bg()
    draw_title("Deterministic multi-signal ranking, not black-box matching")
    
    draw_card(50, height - 450, width - 100, 320, "Components:", [
        "- TF-IDF lexical recall",
        "- Structured AI skill score",
        "- Skill trust: proficiency, duration, endorsements",
        "- Career relevance with recency weighting",
        "- Production / MLOps evidence",
        "- Evaluation / experimentation evidence",
        "- Redrob behavioral availability",
        "- Location / relocation",
        "- Risk penalties",
        "- RRF fusion + deterministic tie-break"
    ])
    
    c.setFillColor(secondary_accent)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 60, "Sort = score descending, then candidate_id ascending.")
    c.showPage()

    # SLIDE 6
    draw_bg()
    draw_title("Every recommendation is auditable")
    
    w = (width - 150) / 2
    draw_card(50, height - 350, w, 200, "Main proof:", [
        "Reasoning must include actual:",
        "- current title",
        "- YOE",
        "- location",
        "- matched AI/retrieval terms",
        "- production/eval evidence",
        "- Redrob response/open/relocation signal"
    ])
    
    draw_card(50 + w + 50, height - 350, w, 200, "Validation cards:", [
        "- Official validator passed",
        "- Internal validator passed",
        "- Forensic audit passed",
        "- 0 hallucination/rule failures",
        "- 74 unique scores",
        "- 100 unique reasonings"
    ])
    
    c.setFillColor(light_text)
    c.setFont("Helvetica", 14)
    c.drawString(50, 90, "No LLM-generated justifications. Explanations are deterministic and evidence-grounded.")
    c.showPage()

    # SLIDE 7
    draw_bg()
    draw_title("From raw candidate pool to validated submission")
    
    # Workflow diagram using text
    c.setFillColor(text_color)
    c.setFont("Helvetica-Bold", 16)
    steps = [
        "Candidate JSONL", "Stream Reader", "Feature Extractor", "Risk Detector",
        "TF-IDF + Structured Scorer", "RRF Ranker", "Grounded Reasoning",
        "Top-100 CSV", "Validator", "Dashboard + Sandbox"
    ]
    
    y = height - 150
    for i, step in enumerate(steps):
        c.drawString(100 + (i % 2) * 350, y, f"→ {step}")
        if i % 2 == 1:
            y -= 40
            
    c.setFillColor(light_text)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 80, "Offline | CPU-only | no raw data committed | reproducible")
    c.showPage()

    # SLIDE 8
    draw_bg()
    draw_title("Local-first architecture built for privacy and reproducibility")
    
    w = (width - 200) / 3
    draw_card(50, height - 400, w, 250, "CLI Ranker:", [
        "rank.py,",
        "stream_candidates,",
        "feature extraction,",
        "scoring,",
        "CSV writer,",
        "reports."
    ])
    draw_card(50 + w + 50, height - 400, w, 250, "Audit Layer:", [
        "validate_submission.py,",
        "internal validation,",
        "forensic_audit.py,",
        "security scans."
    ])
    draw_card(50 + w*2 + 100, height - 400, w, 250, "Interfaces:", [
        "React/Vite dashboard",
        "reads reports/*.json.",
        "",
        "Streamlit sandbox runs",
        "sample candidates locally."
    ])
    
    draw_metric_strip(["No external APIs", "no keys", "no LLM calls", "no backend upload of 100K data"])
    c.showPage()

    # SLIDE 9
    draw_bg()
    draw_title("Final output surfaces real AI/ML/retrieval profiles")
    
    draw_card(50, height - 250, width - 100, 100, "Metrics", [
        "100,000 candidates processed | 100 ranked candidates | 74 unique scores | 100 unique reasonings",
        "0 hallucination failures | CSV validator passed | Under 5 MB output"
    ])
    
    draw_card(50, height - 480, width - 100, 200, "Top candidate preview table:", [
        "1. CAND_0018499 — Senior ML Engineer — 7.2 YOE — Noida",
        "2. CAND_0005260 — Senior NLP Engineer — 5.2 YOE — Chennai",
        "3. CAND_0046525 — Senior ML Engineer — 6.1 YOE — Pune",
        "4. CAND_0081846 — Lead AI Engineer — 6.7 YOE — Jaipur",
        "5. CAND_0042506 — Search Engineer — 4.2 YOE — Mumbai"
    ])
    c.showPage()

    # SLIDE 10
    draw_bg()
    draw_title("Built like an evaluator-proof submission package")
    
    w = (width - 200) / 3
    draw_card(50, height - 400, w, 250, "Tech:", [
        "- Python",
        "- scikit-learn TF-IDF",
        "- deterministic JSONL streaming",
        "- React + Vite dashboard",
        "- Streamlit sandbox"
    ])
    draw_card(50 + w + 50, height - 400, w, 250, "Quality:", [
        "- pytest / coverage",
        "- ruff",
        "- Bandit",
        "- pip-audit",
        "- npm audit",
        "- forensic audit"
    ])
    draw_card(50 + w*2 + 100, height - 400, w, 250, "Security:", [
        "- no raw dataset committed",
        "- no LLM/API dependency",
        "- no secrets",
        "- local CPU execution",
        "- sample sandbox only,",
        "  no full dataset upload"
    ])
    c.showPage()

    # SLIDE 11
    draw_bg()
    draw_title("Submission package")
    
    draw_card(50, height - 380, width - 100, 250, "Submission Assets", [
        "GitHub Repo: https://github.com/Sauravssoni/Screener",
        "Ranked CSV: submissions/submission.csv",
        "Deck PDF: docs/RedrobRank_Official_Submission_Deck.pdf",
        "Methodology PDF: docs/RedrobRank_Methodology.pdf",
        "Audit: reports/final_ranking_audit.md",
        "Sandbox: streamlit run sandbox_app.py",
        "Dashboard: npm run dev"
    ])
    
    c.setFillColor(accent_color)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 450, "RedrobRank is not just a ranking script — it is a reproducible, auditable TalentOps engine.")
    c.showPage()

    c.save()

if __name__ == "__main__":
    create_deck()
