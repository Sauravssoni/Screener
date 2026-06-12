import os
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_deck():
    os.makedirs("docs", exist_ok=True)
    width, height = 13.333 * inch, 7.5 * inch
    c = canvas.Canvas("docs/RedrobRank_Official_Submission_Deck.pdf", pagesize=(width, height))

    bg_color = colors.HexColor("#F9FAFB")
    text_color = colors.HexColor("#1F2937")
    accent_color = colors.HexColor("#DC2626") # Red
    secondary_accent = colors.HexColor("#6D28D9") # Purple
    card_bg = colors.HexColor("#FFFFFF")
    light_text = colors.HexColor("#4B5563")

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=34,
        textColor=text_color,
        leading=40,
        alignment=0,
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=18,
        textColor=text_color,
        leading=24,
    )

    card_title_style = ParagraphStyle(
        'CardTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=text_color,
        leading=22,
    )
    
    card_body_style = ParagraphStyle(
        'CardBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=16,
        textColor=light_text,
        leading=20,
    )

    def draw_bg():
        c.setFillColor(bg_color)
        c.rect(0, 0, width, height, fill=1, stroke=0)
        c.setFillColor(accent_color)
        c.rect(0, height - 12, width, 12, fill=1, stroke=0)

    def draw_title(title_text):
        p = Paragraph(title_text, title_style)
        f = Frame(0.65*inch, height - 2*inch, width - 1.3*inch, 1.5*inch, showBoundary=0, leftPadding=0, bottomPadding=0, topPadding=0)
        f.addFromList([p], c)
        
        c.setStrokeColor(secondary_accent)
        c.setLineWidth(3)
        c.line(0.65*inch, height - 1.6*inch, 2.5*inch, height - 1.6*inch)

    def draw_footer(text):
        p = Paragraph(text, ParagraphStyle('Footer', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=14, textColor=secondary_accent))
        f = Frame(0.65*inch, 0.2*inch, width - 1.3*inch, 0.5*inch, showBoundary=0, leftPadding=0, bottomPadding=0, topPadding=0)
        f.addFromList([p], c)

    def draw_card(x, y, w, h, title, body_text, title_color=text_color):
        c.setFillColor(card_bg)
        c.setStrokeColor(colors.HexColor("#E5E7EB"))
        c.setLineWidth(1)
        c.roundRect(x, y, w, h, 6, fill=1, stroke=1)
        
        ct_style = ParagraphStyle('CT', parent=card_title_style, textColor=title_color)
        p_title = Paragraph(title, ct_style)
        p_body = Paragraph(body_text.replace("\n", "<br/>"), card_body_style)
        
        f = Frame(x + 10, y + 10, w - 20, h - 20, showBoundary=0, leftPadding=0, bottomPadding=0, topPadding=0)
        f.addFromList([p_title, p_body], c)

    def draw_metric_strip(labels):
        strip_h = 45
        strip_y = 0.65 * inch
        c.setFillColor(secondary_accent)
        c.rect(0.65*inch, strip_y, width - 1.3*inch, strip_h, fill=1, stroke=0)
        
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 14)
        
        usable_w = width - 1.3*inch
        segment = usable_w / len(labels)
        for i, label in enumerate(labels):
            cx = 0.65*inch + (i + 0.5) * segment
            c.drawCentredString(cx, strip_y + 16, label)

    # SLIDE 1
    draw_bg()
    
    t_style = ParagraphStyle('T1', parent=title_style, fontSize=46, leading=55, alignment=1)
    p_style = ParagraphStyle('T2', parent=body_style, fontSize=22, textColor=light_text, alignment=1)
    
    f1 = Frame(1*inch, height/2, width - 2*inch, 3*inch, showBoundary=0)
    f1.addFromList([Paragraph("RedrobRank<br/>Agentic Recruiter OS", t_style)], c)
    
    f2 = Frame(1*inch, height/2 - 1.5*inch, width - 2*inch, 1*inch, showBoundary=0)
    f2.addFromList([Paragraph("Grounded candidate discovery for Redrob’s Data & AI Challenge", p_style)], c)
    
    # Small card
    draw_card(width/2 - 200, height/2 - 3.2*inch, 400, 1.4*inch, "", 
              "<b>Team ID:</b> Syntheon<br/><b>Team Name:</b> Syntheon<br/><b>Team Leader:</b> Saurav Soni<br/><b>Problem:</b> Intelligent Candidate Discovery")
    c.showPage()

    # SLIDE 2
    draw_bg()
    draw_title("AI Talent Discovery Is Not Keyword Search")
    
    w = (width - 2.3*inch) / 2
    draw_card(0.65*inch, height - 4.5*inch, w, 1.8*inch, "1. Keyword stuffing", "AI terms appear without real engineering depth.")
    draw_card(0.65*inch + w + 1*inch, height - 4.5*inch, w, 1.8*inch, "2. Ghost candidates", "Profiles may be inactive, unavailable, or low-response.")
    draw_card(0.65*inch, height - 6.8*inch, w, 1.8*inch, "3. Domain mismatch", "Support, accounting, HR, content, or operations roles can contain AI language.")
    draw_card(0.65*inch + w + 1*inch, height - 6.8*inch, w, 1.8*inch, "4. Hallucinated reasons", "A ranking system loses trust when the reason does not match candidate facts.")
    
    draw_footer("RedrobRank optimizes relevance, trust, and reproducibility.")
    c.showPage()

    # SLIDE 3
    draw_bg()
    draw_title("From 100K Profiles to a Grounded Top-100")
    
    w = (width - 2.5*inch) / 4
    draw_card(0.65*inch, height - 4.5*inch, w, 2*inch, "1. Extract Evidence", "Title, YOE, location, career, skills, Redrob behavioral signals.")
    # arrow
    c.setFillColor(accent_color)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(0.65*inch + w + 0.1*inch, height - 3.5*inch, "→")
    
    draw_card(0.65*inch + w + 0.4*inch, height - 4.5*inch, w, 2*inch, "2. Score Fit", "AI/retrieval, production, evaluation, systems, YOE, location, behavior.")
    c.drawString(0.65*inch + 2*w + 0.5*inch, height - 3.5*inch, "→")
    
    draw_card(0.65*inch + 2*w + 0.8*inch, height - 4.5*inch, w, 2*inch, "3. Filter Risk", "Honeypots, keyword stuffers, non-fit roles, manager-only.")
    c.drawString(0.65*inch + 3*w + 0.9*inch, height - 3.5*inch, "→")
    
    draw_card(0.65*inch + 3*w + 1.2*inch, height - 4.5*inch, w, 2*inch, "4. Explain Output", "Every reason references actual candidate facts.")
    
    draw_metric_strip(["100K processed", "100 final rows", "CPU-only", "No LLM/API", "Validator passed"])
    c.showPage()

    # SLIDE 4
    draw_bg()
    draw_title("What the Senior AI Engineer JD Needs")
    
    w = (width - 2.3*inch) / 2
    draw_card(0.65*inch, height - 6.5*inch, w, 4*inch, "✓ Must-have signals", 
              "- Retrieval / vector search / semantic search<br/>"
              "- Ranking / recommendation systems<br/>"
              "- LLM / RAG / fine-tuning / NLP<br/>"
              "- Production ML / MLOps<br/>"
              "- Evaluation: NDCG, MRR, A/B testing<br/>"
              "- Python + data/systems infrastructure", title_color=colors.HexColor("#059669"))
              
    draw_card(0.65*inch + w + 1*inch, height - 6.5*inch, w, 4*inch, "⚠️ Risk signals", 
              "- Non-technical role mismatch<br/>"
              "- Prompt-only or keyword-stuffed profiles<br/>"
              "- Manager-only with weak technical depth<br/>"
              "- Pure research without production evidence<br/>"
              "- Weak availability or response behavior", title_color=accent_color)
    c.showPage()

    # SLIDE 5
    draw_bg()
    draw_title("Deterministic Multi-Signal Ranking")
    
    draw_card(0.65*inch, height - 6.5*inch, width - 1.3*inch, 4.2*inch, "Scoring Stack:", 
        "1. TF-IDF lexical recall<br/>"
        "2. Structured AI skill score<br/>"
        "3. Skill trust: proficiency, duration, endorsements<br/>"
        "4. Career relevance with recency weighting<br/>"
        "5. Production + evaluation evidence<br/>"
        "6. Behavioral availability<br/>"
        "7. Risk penalties<br/>"
        "8. RRF fusion + candidate_id tie-break"
    )
    
    draw_footer("No black-box ranking. No hidden API calls. Same input, same output.")
    c.showPage()

    # SLIDE 6
    draw_bg()
    draw_title("Every Recommendation Is Auditable")
    
    w = (width - 2.3*inch) / 2
    draw_card(0.65*inch, height - 5.5*inch, w, 3*inch, "Reasoning uses actual:", 
        "- Current title<br/>"
        "- YOE<br/>"
        "- Location<br/>"
        "- Matched AI/retrieval terms<br/>"
        "- Production/eval evidence<br/>"
        "- Redrob behavioral signals"
    )
    
    draw_card(0.65*inch + w + 1*inch, height - 5.5*inch, w, 3*inch, "Metrics & Proof:", 
        "- Official validator: Passed<br/>"
        "- Internal validator: Passed<br/>"
        "- Forensic audit: Passed<br/>"
        "- Hallucination failures: 0<br/>"
        "- Unique scores: 74<br/>"
        "- Unique reasonings: 100"
    )
    
    draw_footer("No LLM-generated justifications. Explanations are deterministic and evidence-grounded.")
    c.showPage()

    # SLIDE 7
    draw_bg()
    draw_title("End-to-End Workflow")
    
    p = Paragraph(
        "<b>Candidate JSONL</b> &nbsp;→&nbsp; "
        "<b>Stream Reader</b> &nbsp;→&nbsp; "
        "<b>Feature Extractor</b> &nbsp;→&nbsp; "
        "<b>Risk Detector</b><br/><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br/><br/>"
        "<b>TF-IDF + Structured Scorer</b> &nbsp;→&nbsp; "
        "<b>RRF Ranker</b> &nbsp;→&nbsp; "
        "<b>Grounded Reasoning</b><br/><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓<br/><br/>"
        "<b>Top-100 CSV</b> &nbsp;→&nbsp; "
        "<b>Validator</b> &nbsp;→&nbsp; "
        "<b>Dashboard / Sandbox</b>",
        ParagraphStyle('Pipe', parent=body_style, fontSize=20, leading=26, alignment=1)
    )
    f = Frame(0.65*inch, height - 6.5*inch, width - 1.3*inch, 4*inch, showBoundary=0)
    f.addFromList([p], c)
    
    draw_footer("Offline | CPU-only | no raw data committed | reproducible")
    c.showPage()

    # SLIDE 8
    draw_bg()
    draw_title("Local-First, Privacy-First Architecture")
    
    w = (width - 2.3*inch) / 3
    draw_card(0.65*inch, height - 5.5*inch, w, 3*inch, "CLI Ranker:", "rank.py, stream reader, feature extractor, scorer, CSV writer, reports")
    draw_card(0.65*inch + w + 0.5*inch, height - 5.5*inch, w, 3*inch, "Audit Layer:", "validator, forensic audit, security scans, quality reports")
    draw_card(0.65*inch + 2*w + 1*inch, height - 5.5*inch, w, 3*inch, "Interfaces:", "React/Vite dashboard, Streamlit sample sandbox")
    
    draw_metric_strip(["No external APIs", "No keys", "No LLM calls", "No full dataset browser upload"])
    c.showPage()

    # SLIDE 9
    draw_bg()
    draw_title("Final Output Surfaces Real AI Profiles")
    
    draw_card(0.65*inch, height - 3.5*inch, width - 1.3*inch, 1*inch, "", 
        "100,000 processed | 100 ranked | 74 unique scores | 100 unique reasonings<br/>"
        "0 hallucination failures | CSV validator passed | Under 5 MB output"
    )
    
    data = [
        ["CAND_0018499", "Senior ML Engineer", "7.2 YOE", "Noida"],
        ["CAND_0005260", "Senior NLP Engineer", "5.2 YOE", "Chennai"],
        ["CAND_0046525", "Senior ML Engineer", "6.1 YOE", "Pune"],
        ["CAND_0081846", "Lead AI Engineer", "6.7 YOE", "Jaipur"],
        ["CAND_0042506", "Search Engineer", "4.2 YOE", "Mumbai"]
    ]
    
    t = Table(data, colWidths=[1.8*inch, 4*inch, 1.5*inch, 1.5*inch])
    t.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 16),
        ('TEXTCOLOR', (0,0), (-1,-1), text_color),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('LINEBELOW', (0,0), (-1,-1), 1, colors.HexColor("#E5E7EB")),
    ]))
    
    t.wrapOn(c, width, height)
    t.drawOn(c, 0.65*inch + 0.2*inch, height - 6.8*inch)
    
    c.showPage()

    # SLIDE 10
    draw_bg()
    draw_title("Evaluator-Proof by Design")
    
    w = (width - 2.3*inch) / 3
    draw_card(0.65*inch, height - 5.5*inch, w, 3*inch, "Tech:", 
        "- Python<br/>"
        "- scikit-learn TF-IDF<br/>"
        "- JSONL streaming<br/>"
        "- React/Vite<br/>"
        "- Streamlit"
    )
    draw_card(0.65*inch + w + 0.5*inch, height - 5.5*inch, w, 3*inch, "Quality:", 
        "- pytest, coverage<br/>"
        "- ruff<br/>"
        "- forensic audit<br/>"
        "- validator checks"
    )
    draw_card(0.65*inch + 2*w + 1*inch, height - 5.5*inch, w, 3*inch, "Security:", 
        "- Bandit, pip-audit, npm audit<br/>"
        "- no secrets<br/>"
        "- no raw data<br/>"
        "- no LLM/API"
    )
    
    draw_footer("Built for reproducibility, not demo theater.")
    c.showPage()

    # SLIDE 11
    draw_bg()
    draw_title("Final Submission Package")
    
    draw_card(0.65*inch, height - 5.5*inch, width - 1.3*inch, 3*inch, "", 
        "<b>Team ID:</b> Syntheon<br/>"
        "<b>Team Name:</b> Syntheon<br/>"
        "<b>GitHub Repo:</b> https://github.com/Sauravssoni/Screener<br/>"
        "<b>Ranked CSV:</b> submissions/submission.csv<br/>"
        "<b>Deck PDF:</b> docs/RedrobRank_Official_Submission_Deck.pdf<br/>"
        "<b>Methodology PDF:</b> docs/RedrobRank_Methodology.pdf<br/>"
        "<b>Audit:</b> reports/final_ranking_audit.md<br/>"
        "<b>Dashboard:</b> npm run dev<br/>"
        "<b>Sandbox:</b> streamlit run sandbox_app.py"
    )
    
    # Very safe margin and wrapped closing statement
    p_close = Paragraph(
        "RedrobRank is a reproducible, auditable TalentOps engine —<br/>not just a ranking script.",
        ParagraphStyle('Close', parent=body_style, fontName='Helvetica-Bold', fontSize=22, textColor=accent_color, alignment=1)
    )
    f_close = Frame(0.65*inch, 0.5*inch, width - 1.3*inch, 1.5*inch, showBoundary=0)
    f_close.addFromList([p_close], c)
    
    c.showPage()

    c.save()

if __name__ == "__main__":
    create_deck()
