import pdfplumber
import re

# Extract text from PDF
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# Extract fields (Amount, Date)
def extract_fields(text):
    amount = re.findall(r'\d+(?:,\d{3})*(?:\.\d{2})?', text)
    date = re.findall(r'\d{2}/\d{2}/\d{4}', text)

    return {
        "Amount": amount[0] if amount else "Not Found",
        "Date": date[0] if date else "Not Found"
    }


# Risk Detection
def detect_risk(text, fields):
    risk_score = 0
    reasons = []

    if fields["Amount"] == "Not Found":
        risk_score += 2
        reasons.append("Missing amount")

    if "urgent" in text.lower():
        risk_score += 2
        reasons.append("Contains 'urgent' keyword")

    if "confidential" in text.lower():
        risk_score += 2
        reasons.append("Contains 'confidential' keyword")

    if risk_score >= 4:
        level = "HIGH"
    elif risk_score >= 2:
        level = "MEDIUM"
    else:
        level = "LOW"

    return level, reasons


# Simple Summary (NO API)
def generate_summary(text):
    summary = text[:300]  # first 300 characters

    if "urgent" in text.lower():
        summary += "\n\n⚠️ Risk: Contains urgent request"

    if "confidential" in text.lower():
        summary += "\n⚠️ Risk: Contains confidential keyword"

    return summary