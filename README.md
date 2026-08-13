# 🎯 AI Career Advisor

An **AI-powered Career & Skill Recommendation System** that analyzes a student's academic profile, technical skills, projects, and internship experience to recommend suitable technology career paths.

The system also performs **skill-gap analysis** and generates a **personalized 12-week learning roadmap**.

---

## 🚀 Features

* 🎯 AI-based career recommendation
* 📊 Top 3 career-match predictions
* 🔍 Skill-gap analysis
* 📚 Personalized learning roadmap
* 💡 Recommended projects based on career path
* 🤖 Machine Learning prediction using Random Forest
* 🌐 Interactive Streamlit web application
* 📈 Career match visualization
* ⚡ Simple and beginner-friendly interface

---

## 🧠 How It Works

```text
Student Profile
      │
      ├── CGPA
      ├── Technical Skills
      ├── Projects
      └── Internship Experience
              │
              ▼
       Machine Learning Model
              │
              ▼
       Career Prediction
              │
       ┌──────┼────────┐
       ▼      ▼        ▼
    Career  Skill    Project
    Match    Gap    Suggestions
       │      │        │
       └──────┼────────┘
              ▼
     12-Week Learning Roadmap
```

---

## 💼 Career Paths

The current prototype supports recommendations for:

* Data Scientist
* Machine Learning Engineer
* Data Analyst
* AI Engineer
* Software Developer

---

## 🛠️ Tech Stack

| Technology    | Purpose               |
| ------------- | --------------------- |
| Python        | Programming Language  |
| Pandas        | Data Processing       |
| NumPy         | Numerical Computing   |
| Scikit-learn  | Machine Learning      |
| Random Forest | Career Classification |
| Streamlit     | Web Application       |
| Git & GitHub  | Version Control       |

---

## 📁 Project Structure

```text
AI-Career-Advisor/
│
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── .gitignore
│
├── data/
│
└── model/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Career-Advisor.git
```

### 2. Open the project

```bash
cd AI-Career-Advisor
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 📊 Example Workflow

1. Enter your CGPA.
2. Enter the number of projects completed.
3. Select your current technical skills.
4. Select whether you have internship experience.
5. Click **Analyze My Career**.
6. The system predicts suitable career paths.
7. Review your skill gaps.
8. Follow the generated learning roadmap.

---

## 🤖 Machine Learning

The project currently uses a **Random Forest Classifier**.

### Input Features

* Python
* SQL
* Statistics
* Pandas
* Machine Learning
* Data Visualization
* Deep Learning
* Git
* APIs
* NLP
* DSA
* OOP
* Excel
* Power BI
* Scikit-learn
* Problem Solving
* CGPA
* Number of Projects
* Internship Experience

### Output

The model predicts the most suitable career category based on the student's profile.

---

## 📚 Skill Gap Analysis

After predicting the career, the system compares the student's current skills against the skills required for that career.

For example:

```text
Recommended Career: ML Engineer

Current Skills:
✅ Python
✅ Machine Learning
✅ Git

Skills to Learn:
📌 Deep Learning
📌 Scikit-learn
📌 APIs
```

---

## 🗺️ Personalized Roadmap

The application provides a 12-week learning roadmap covering:

```text
Weeks 1–2   → Python, OOP & Git
Weeks 3–4   → SQL & Data Handling
Weeks 5–6   → Statistics & Machine Learning
Weeks 7–8   → Domain-focused ML Project
Weeks 9–10  → APIs & Deployment
Weeks 11–12 → GitHub, Resume & Interview Preparation
```

---

## 📈 Future Improvements

The current version is a working prototype. Future versions can include:

* [ ] Real-world student/career dataset
* [ ] Resume PDF parsing
* [ ] NLP-based skill extraction
* [ ] Real-time job recommendations
* [ ] Course recommendations
* [ ] User authentication
* [ ] Database integration
* [ ] Student progress tracking
* [ ] Advanced recommendation algorithms
* [ ] Explainable AI
* [ ] Cloud deployment
* [ ] Job-market trend analysis

---

## ⚠️ Dataset Note

The current prototype uses **synthetically generated training data** so that the application can run immediately without requiring an external dataset.

For an academic/research-grade version, the synthetic dataset should be replaced with a properly collected and validated real-world dataset.

Therefore, the current predictions should be treated as a **project demonstration**, not as professional career advice.

---

## 🎓 Academic Project

**Project:** AI-Based Career & Skill Recommendation System

**Domain:** Artificial Intelligence & Machine Learning

**Technologies:** Python, Machine Learning, Scikit-learn, Streamlit

**Model:** Random Forest Classifier

---

## 👨‍💻 Author

**Yelipe Rishi**

B.Tech — Artificial Intelligence & Machine Learning

Aditya Engineering College

---

## ⭐ If You Like This Project

If this project helped you understand end-to-end machine learning development, consider giving the repository a ⭐.

---

## 📄 License

This project is created for educational and academic purposes.
