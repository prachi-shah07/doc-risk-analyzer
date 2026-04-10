import streamlit as st
from utils import extract_text, extract_fields, detect_risk, generate_summary

st.set_page_config(page_title="AI Document Risk Analyzer")

st.title("📄 AI Document Risk Analyzer")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:

    st.info("Processing document...")

    text = extract_text(uploaded_file)

    st.subheader("📜 Extracted Text")
    st.write(text[:500])

    fields = extract_fields(text)

    st.subheader("📊 Extracted Fields")
    st.write(fields)

    risk_level, reasons = detect_risk(text, fields)

    st.subheader("⚠️ Risk Analysis")
    st.write(f"Risk Level: **{risk_level}**")
    st.write("Reasons:", reasons)

    st.subheader("🧠 Summary")
    summary = generate_summary(text)
    st.write(summary)