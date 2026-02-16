import sys
from pathlib import Path

try:
    from PyPDF2 import PdfReader
except Exception as e:
    print("ERROR: PyPDF2 not installed")
    raise

if len(sys.argv) < 2:
    print("Usage: python extract_pdf.py <pdf-path>")
    sys.exit(1)

pdf_path = Path(sys.argv[1])
if not pdf_path.exists():
    print(f"ERROR: File not found: {pdf_path}")
    sys.exit(1)

reader = PdfReader(str(pdf_path))
text_parts = []
for page in reader.pages:
    try:
        text_parts.append(page.extract_text() or '')
    except Exception:
        pass

text = "\n\n".join(text_parts).strip()
print("===PDF_TEXT_START===")
print(text)
print("===PDF_TEXT_END===")
