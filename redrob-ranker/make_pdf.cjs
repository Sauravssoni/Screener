const PDFDocument = require('pdfkit');
const fs = require('fs');

const doc = new PDFDocument();
doc.pipe(fs.createWriteStream('redrob-ranker/docs/RedrobRank_Methodology.pdf'));

doc.fontSize(25).text('RedrobRank Methodology', 100, 100);
doc.fontSize(14).text('1. Problem: Keyword filters miss true fit.', 100, 150);
doc.text('2. Role Understanding: Senior AI Engineer.', 100, 180);
doc.text('3. System Architecture: JSONL stream -> feature extraction -> scoring.', 100, 210);
doc.text('4. Feature Families: Core AI, Production, Evaluation, Behavioral.', 100, 240);
doc.text('5. Honeypot Defense: Strict traps via rule-based matching.', 100, 270);
doc.text('6. Behavioral: Response rate usage.', 100, 300);
doc.text('7. Explainability: Generated reasoning strings mapped to raw JSON.', 100, 330);
doc.text('8. Reproducibility: 15s latency on CPU-only.', 100, 360);
doc.text('9. Output validated correctly.', 100, 390);

doc.end();
