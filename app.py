import streamlit as st
from utils import extract_text, extract_fields, detect_risk, generate_summary

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Document Risk Analyzer",
    page_icon="📄",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #4CAF50;
}

.subtitle {
    text-align: center;
    color: #A0A0A0;
    font-size: 20px;
    margin-bottom: 30px;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #161B22;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120
    )

    st.title("📌 About")

    st.write("""
    AI-powered platform for:
    - Document Analysis
    - Risk Detection
    - Text Summarization
    - NLP Processing
    """)

    st.markdown("---")

    st.subheader("⚙️ Supported Files")
    st.write("✅ PDF Documents")

    st.markdown("---")

    st.subheader("🛠️ Tech Stack")
    st.write("""
    - Python
    - Streamlit
    - NLP
    - PyPDF2
    - Scikit-learn
    """)

# ---------------- HERO SECTION ---------------- #

st.title("📄 AI Document Risk Analyzer")

st.subheader(
    "AI-powered platform for intelligent document analysis, risk detection, and automated summarization."
)

# ---------------- FEATURE CARDS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📄 Document Extraction")

with col2:
    st.warning("⚠️ Risk Detection")

with col3:
    st.success("🧠 AI Summarization")

st.markdown("---")

# ---------------- FILE UPLOAD ---------------- #

st.markdown("### 📂 Upload Your Document")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"],
    help="Upload PDF document for analysis",
    label_visibility="collapsed"
)

# ---------------- PROCESS DOCUMENT ---------------- #

if uploaded_file:

    with st.spinner("🔍 Analyzing document... Please wait"):

        text = extract_text(uploaded_file)

        fields = extract_fields(text)

        risk_level, reasons = detect_risk(text, fields)

        summary = generate_summary(text)

    st.success("✅ Document Processed Successfully")

    # ---------------- METRICS ---------------- #

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Text Length", f"{len(text)} chars")

    with col2:
        st.metric("📊 Fields Extracted", len(fields))

    with col3:
        st.metric("⚠️ Risk Level", risk_level)

    # ---------------- RISK SCORE ---------------- #

    if risk_level.lower() == "high":
        risk_score = 85
    elif risk_level.lower() == "medium":
        risk_score = 55
    else:
        risk_score = 20

    st.markdown("### 📈 Risk Score")

    st.progress(risk_score)

    st.caption(f"Risk Score: {risk_score}%")

    st.markdown("---")

    # ---------------- TABS ---------------- #

    tab1, tab2, tab3 = st.tabs([
        "📜 Extracted Text",
        "⚠️ Risk Analysis",
        "🧠 Summary"
    ])

    # ---------------- TAB 1 ---------------- #

    with tab1:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.write(text[:3000])

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 2 ---------------- #

    with tab2:

        if risk_level.lower() == "high":
            st.error("🚨 High Risk Detected")

        elif risk_level.lower() == "medium":
            st.warning("⚠️ Medium Risk Detected")

        else:
            st.success("✅ Low Risk Detected")

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📊 Extracted Information")

        st.json(fields)

        st.subheader("⚠️ Risk Reasons")

        for reason in reasons:
            st.write(f"• {reason}")

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- TAB 3 ---------------- #

    with tab3:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.write(summary)

        st.markdown('</div>', unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

# ---------------- FOOTER ---------------- #

st.markdown("""
<hr>
<center>
    <p style='color:gray'>
        Developed by Prachi Shah • AI + NLP Project • Streamlit
    </p>
</center>
""", unsafe_allow_html=True)