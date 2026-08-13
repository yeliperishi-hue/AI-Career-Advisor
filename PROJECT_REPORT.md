# AI-Based Career & Skill Recommendation System

## 1. Abstract
The AI Career Advisor is an end-to-end machine learning application designed to help students identify suitable technology career paths from their current skills and academic/project profile. The system predicts career categories, highlights missing skills, and provides a structured learning roadmap.

## 2. Problem Statement
Students often have difficulty selecting a career path because technology roles require overlapping but different skill sets. A recommendation system can organize a student's current profile and suggest a direction.

## 3. Objectives
- Predict a suitable career category.
- Show alternative career matches.
- Identify skill gaps.
- Provide a practical learning roadmap.
- Demonstrate deployment of an ML model through a web interface.

## 4. Methodology
1. Define career categories and required skills.
2. Create/collect a labeled dataset.
3. Clean and encode features.
4. Train classification models.
5. Evaluate the selected model.
6. Integrate the model into a Streamlit application.
7. Deploy and test the application.

## 5. Current Prototype
This repository uses synthetic training data so it can run without an external dataset. The model is a Random Forest classifier.

## 6. Future Scope
- Use a large validated student/skills dataset.
- Add resume parsing.
- Add job-market data.
- Add recommendation explanations.
- Add user accounts and progress tracking.
- Add real-time course/job recommendations.

## 7. Limitations
Career prediction is only a recommendation and should not be treated as a definitive assessment. Synthetic training data is suitable for demonstrating the software pipeline but not for making real-world claims.
