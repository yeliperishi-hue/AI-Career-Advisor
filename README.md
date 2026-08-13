# AI Career Advisor 🎯

An end-to-end AIML portfolio project that predicts a suitable career path from a student's skills and profile, performs skill-gap analysis, and generates a 12-week learning roadmap.

## Features
- Career prediction using Random Forest
- Top-3 career match visualization
- Skill-gap analysis
- Personalized roadmap
- Project recommendations
- Streamlit web interface

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Streamlit

## Run locally

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
streamlit run app.py
```

The app will open in your browser.

## Important
The included training data is synthetically generated so the project is immediately runnable. For a final academic/research version, replace it with a properly collected and validated dataset and report the methodology, limitations, and evaluation metrics.
