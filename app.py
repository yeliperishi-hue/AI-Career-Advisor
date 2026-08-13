import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="AI Career Advisor", page_icon="🎯", layout="wide")

CAREER_SKILLS = {
    "Data Scientist": ["Python", "SQL", "Statistics", "Pandas", "Machine Learning", "Data Visualization"],
    "ML Engineer": ["Python", "Machine Learning", "Scikit-learn", "Deep Learning", "Git", "APIs"],
    "Data Analyst": ["Python", "SQL", "Excel", "Statistics", "Power BI", "Data Visualization"],
    "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "NLP", "APIs", "Git"],
    "Software Developer": ["Python", "DSA", "OOP", "SQL", "Git", "Problem Solving"],
}

ALL_SKILLS = sorted(set(sum(CAREER_SKILLS.values(), [])))

def make_training_data():
    rows = []
    rng = np.random.default_rng(42)
    profiles = {
        "Data Scientist": ["Python","SQL","Statistics","Pandas","Machine Learning","Data Visualization"],
        "ML Engineer": ["Python","Machine Learning","Scikit-learn","Deep Learning","Git","APIs"],
        "Data Analyst": ["Python","SQL","Excel","Statistics","Power BI","Data Visualization"],
        "AI Engineer": ["Python","Machine Learning","Deep Learning","NLP","APIs","Git"],
        "Software Developer": ["Python","DSA","OOP","SQL","Git","Problem Solving"],
    }
    for career, strong in profiles.items():
        for _ in range(180):
            row = {}
            for skill in ALL_SKILLS:
                base = 0.82 if skill in strong else 0.18
                row[skill] = int(rng.random() < base)
            row["CGPA"] = round(float(np.clip(rng.normal(7.8, 1.0), 5.5, 10)), 2)
            row["Projects"] = int(np.clip(rng.poisson(2), 0, 6))
            row["Internship"] = int(rng.random() < 0.45)
            row["Career"] = career
            rows.append(row)
    return pd.DataFrame(rows)

@st.cache_resource
def train_model():
    df = make_training_data()
    X = df.drop(columns=["Career"])
    y = df["Career"]
    model = RandomForestClassifier(n_estimators=300, random_state=42, max_depth=12)
    model.fit(X, y)
    return model

model = train_model()

st.title("🎯 AI Career Advisor")
st.caption("A portfolio-ready AIML project that recommends career paths and identifies skill gaps.")

with st.sidebar:
    st.header("Student Profile")
    cgpa = st.slider("CGPA", 5.0, 10.0, 7.5, 0.1)
    projects = st.slider("Number of projects", 0, 10, 2)
    internship = st.checkbox("Completed an internship")
    selected_skills = st.multiselect("Your current skills", ALL_SKILLS)

st.markdown("### 1. Career prediction")

if st.button("🚀 Analyze My Career", use_container_width=True):
    x = {skill: int(skill in selected_skills) for skill in ALL_SKILLS}
    x["CGPA"] = cgpa
    x["Projects"] = projects
    x["Internship"] = int(internship)
    input_df = pd.DataFrame([x])

    probabilities = model.predict_proba(input_df)[0]
    careers = model.classes_
    ranking = pd.DataFrame({"Career": careers, "Match": probabilities})
    ranking = ranking.sort_values("Match", ascending=False).head(3)

    top_career = ranking.iloc[0]["Career"]
    st.session_state["career"] = top_career
    st.session_state["ranking"] = ranking
    st.session_state["skills"] = selected_skills

if "career" in st.session_state:
    career = st.session_state["career"]
    ranking = st.session_state["ranking"]
    selected_skills = st.session_state["skills"]

    c1, c2, c3 = st.columns(3)
    c1.metric("Recommended Career", career)
    c2.metric("Top Match", f"{ranking.iloc[0]['Match']*100:.1f}%")
    c3.metric("Skills Selected", len(selected_skills))

    st.markdown("### 2. Career match")
    chart = ranking.copy()
    chart["Match"] *= 100
    chart = chart.set_index("Career")
    st.bar_chart(chart["Match"])

    required = CAREER_SKILLS[career]
    missing = [s for s in required if s not in selected_skills]
    strong = [s for s in required if s in selected_skills]

    st.markdown("### 3. Skill-gap analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.success("Skills you already have")
        for s in strong:
            st.write(f"✅ {s}")
    with col2:
        st.warning("Skills to learn")
        for s in missing:
            st.write(f"📌 {s}")

    st.markdown("### 4. Personalized 12-week roadmap")
    roadmap = [
        ("Weeks 1–2", "Strengthen Python, OOP and Git"),
        ("Weeks 3–4", "Learn SQL and data handling"),
        ("Weeks 5–6", "Study statistics and machine learning"),
        ("Weeks 7–8", "Build one domain-focused ML project"),
        ("Weeks 9–10", "Learn APIs and deploy the model"),
        ("Weeks 11–12", "Polish GitHub, resume and interview preparation"),
    ]
    for period, task in roadmap:
        st.write(f"**{period}:** {task}")

    st.markdown("### 5. Suggested projects")
    suggestions = {
        "Data Scientist": ["Customer Churn Prediction", "Sales Forecasting", "Recommendation System"],
        "ML Engineer": ["End-to-End ML API", "Fraud Detection API", "Model Monitoring Dashboard"],
        "Data Analyst": ["Sales Analytics Dashboard", "Customer Segmentation", "Business KPI Dashboard"],
        "AI Engineer": ["RAG Question Answering App", "Sentiment Analysis", "AI Document Assistant"],
        "Software Developer": ["Task Management API", "E-commerce Backend", "DSA Practice Platform"],
    }
    for p in suggestions[career]:
        st.write(f"🔹 {p}")

st.divider()
st.caption("Educational project demo. The training data is synthetic; replace it with a validated real dataset before using the system for real career decisions.")
