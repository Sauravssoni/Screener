from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY


def generate_pdf():
    doc = SimpleDocTemplate(
        "docs/RedrobRank_Methodology.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18
    )

    Story = []
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["Normal"]

    Story.append(Paragraph("RedrobRank Agentic Recruiter OS Methodology", title_style))
    Story.append(Spacer(1, 12))

    sections = [
        (
            "1. RedrobRank Agentic Recruiter OS",
            "RedrobRank is an advanced, validated CPU-only TalentOps Agent designed to autonomously screen, evaluate, and rank candidate profiles based on deep semantic matching and deterministic feature extraction.",
        ),
        (
            "2. Problem",
            "Modern recruiting pipelines are flooded with candidates, making it impossible to manually evaluate every profile for specific technical requirements, production experience, and evaluation rigor without introducing bias or missing top talent.",
        ),
        (
            "3. Agent Architecture",
            "The ranker processes candidates using a deterministic, rule-based feature extractor and a highly calibrated weighting algorithm. It extracts text from profile headlines, summaries, and career histories.",
        ),
        (
            "4. Scoring Model",
            "The scoring model is a multi-dimensional weighted sum of extracted features. It parses explicit skills, computes a base score, and modulates it using behavioral signals and risk penalties.",
        ),
        (
            "5. Feature Weights",
            "The algorithm targets: Core AI & Retrieval, Production deployments (MLOps, scaling), Evaluation (NDCG, MAP, A/B testing), and Python/Systems infrastructure. Each category is assigned a specific weight reflecting the job description.",
        ),
        (
            "6. Trap / Honeypot Defense",
            "The system actively detects and penalizes synthetic behaviors, disqualifying candidates who claim 'expert' status with minimal time experience, or keyword stuffers lacking evidence of production deployment.",
        ),
        (
            "7. Human-in-the-loop Workflow",
            "To ensure quality, the agent implements a Human Review Checkpoint. It flags candidates with specific risks or high scores, allowing human recruiters to Approve, Hold, or Reject candidates in a local demo state before any outreach is sent.",
        ),
        (
            "8. Reproducibility",
            "The ranking pipeline is entirely reproducible. The system uses deterministic scoring with candidate_id tie-breaks to ensure that repeated runs yield identical results for the same dataset.",
        ),
        (
            "9. Validation Results",
            "The pipeline was validated against an internal test dataset, strictly adhering to non-increasing score constraints. Synthetic benchmark clusters were successfully detected and properly ordered.",
        ),
        (
            "10. Final Artifacts",
            "The final artifacts include a validated submission.csv containing ranked candidates, a detailed PDF methodology report, and an interactive React dashboard visualizing the pipeline results.",
        ),
    ]

    for title, text in sections:
        Story.append(Paragraph(title, heading_style))
        Story.append(Spacer(1, 6))
        Story.append(Paragraph(text, body_style))
        Story.append(Spacer(1, 12))

    doc.build(Story)


if __name__ == "__main__":
    generate_pdf()
