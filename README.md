# 📄 AI Document Risk Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/NLP-AI_Powered-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

# 🚀 Overview

AI Document Risk Analyzer is an AI-powered web application that intelligently analyzes uploaded PDF documents, extracts meaningful information, detects potential risks, and generates automated summaries using Natural Language Processing (NLP).

The application is designed to simplify document understanding by automating:
- Text Extraction
- Risk Detection
- Information Analysis
- AI-based Summarization

This project demonstrates practical implementation of:
- Artificial Intelligence
- NLP Pipelines
- Streamlit Dashboard Development
- Document Processing Systems
- Risk Analysis Workflows

---

# ✨ Features

✅ Upload and analyze PDF documents  
✅ Automatic text extraction from files  
✅ AI-powered risk detection  
✅ Intelligent summary generation  
✅ Interactive dashboard UI  
✅ Real-time document processing  
✅ Risk score visualization  
✅ Download generated summary  
✅ Dark professional UI theme  
✅ Metrics dashboard for analysis  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Streamlit | Frontend Dashboard |
| NLP | Text Processing |
| PyPDF2 | PDF Text Extraction |
| Scikit-learn | ML Utilities |
| Pandas | Data Handling |
| Matplotlib | Visualization |
| Seaborn | Analytics |

---

# 🏗️ System Workflow

```text
User Uploads PDF
        ↓
Text Extraction
        ↓
NLP Preprocessing
        ↓
Field Extraction
        ↓
Risk Detection
        ↓
Summary Generation
        ↓
Dashboard Visualization
```

---

# 📂 Project Structure

```bash
doc-risk-analyzer/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── screenshots/
│   ├── homepage.png
│   ├── dashboard.png
│
├── uploads/
├── assets/
└── venv/
```

---

# 📸 Application Screenshots

## 🏠 Home Page

![Home Page](screenshots/homepage.png)

---

## 📊 Dashboard & Analysis

![Dashboard](screenshots/dashboard.png)

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/prachi-shah07/doc-risk-analyzer.git
```

---

## 2️⃣ Move into Project Folder

```bash
cd doc-risk-analyzer
```

---

## 3️⃣ Open in VS Code

```bash
code .
```

---

## 4️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate virtual environment:

```bash
.\venv\Scripts\activate
```

---

### Mac/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Required Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt gives any issue:

```bash
pip install streamlit pandas scikit-learn matplotlib seaborn PyPDF2
```

---

## 6️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 7️⃣ Open in Browser

After running the command, Streamlit automatically opens:

```text
http://localhost:8501
```

---

# 🧠 NLP Features Used

- Text Extraction
- Text Cleaning
- Keyword Detection
- Field Extraction
- Risk Classification
- Summary Generation

---

# ⚠️ Risk Detection

The system identifies potential:
- Financial Risks
- Legal Risks
- Sensitive Keywords
- Suspicious Information
- Document-based anomalies

Risk levels are categorized as:
- Low
- Medium
- High

---

# 📊 Dashboard Features

The application dashboard provides:
- Extracted text metrics
- Risk score visualization
- AI-generated summaries
- Field extraction results
- Tab-based navigation
- Downloadable summaries

---

# 📥 Download Summary Feature

Users can download the generated summary directly from the dashboard using the built-in download functionality.

---

# 🔮 Future Enhancements

- OpenAI API Integration
- OCR for scanned PDFs
- Multi-language support
- Cloud deployment
- User authentication
- Advanced AI risk models
- Interactive charts and analytics
- PDF report export

---

# 🛠️ Common Errors & Solutions

## ❌ streamlit not recognized

```bash
pip install streamlit
```

---

## ❌ Python not recognized

Reinstall Python and enable:

```text
Add Python to PATH
```

---

## ❌ requirements.txt issue

```bash
pip install streamlit pandas scikit-learn matplotlib seaborn PyPDF2
```

---

## ❌ Port already in use

```bash
streamlit run app.py --server.port 8502
```

---

# 🧾 Git Commands

## Add Files

```bash
git add .
```

---

## Commit Changes

```bash
git commit -m "Updated project"
```

---

## Push to GitHub

```bash
git push origin main
```

---

# 📚 Learning Outcomes

Through this project, I learned:
- AI-powered document analysis
- NLP pipeline implementation
- Streamlit dashboard design
- PDF text extraction
- Risk detection systems
- Real-world AI application workflows
- Git & GitHub project management

---

# 👩‍💻 Author

## Prachi Shah

B.Tech Computer Science Engineering  
MIT-WPU Pune  

GitHub:  
https://github.com/prachi-shah07

---

# 📄 License

This project is developed for:
- Educational purposes
- Portfolio projects
- AI/NLP learning

---

# ⭐ Conclusion

AI Document Risk Analyzer combines Artificial Intelligence and Natural Language Processing to simplify document understanding and automated risk analysis. The platform provides an interactive and professional dashboard capable of extracting information, detecting risks, and generating intelligent summaries from uploaded documents in real time.