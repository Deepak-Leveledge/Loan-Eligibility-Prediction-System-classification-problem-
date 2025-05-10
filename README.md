## Loan Eligibility Prediction System ------> Calssification Problem

🚀 Loan Eligibility Prediction System
A machine learning-powered web application to assess loan eligibility based on user-provided financial and personal details. Built using Flask and an ensemble of advanced ML models, the system helps lenders quickly evaluate an applicant's creditworthiness.

📌 Overview
The Loan Eligibility Prediction System predicts whether a loan applicant is eligible for a loan using an ensemble of three machine learning models. The application features a user-friendly web interface and is powered by Flask, scikit-learn, CatBoost, and XGBoost.

🧠 Models Used
The prediction engine combines three powerful models to boost accuracy and reliability:

CatBoost Classifier

Handles categorical variables efficiently

Balanced in accuracy and interpretability

XGBoost Classifier

Optimized for numerical data

Known for its speed and performance

Random Forest Classifier

Handles both numerical and categorical features

Robust and interpretable ensemble method

⚙️ Machine Learning Workflow
🔹 1. Data Preprocessing
Handling missing values

Outlier detection and treatment

Feature scaling and encoding

🔹 2. Feature Engineering
Derivation of new features to enhance model learning

🔹 3. Hyperparameter Tuning
Using GridSearchCV for optimal parameter selection:

CatBoost

iterations: 1000

learning_rate: 0.01

depth: 6

l2_leaf_reg: 3

XGBoost

max_depth: 6

learning_rate: 0.01

n_estimators: 1000

gamma: 0.1

Random Forest

n_estimators: 1000

max_depth: 6

min_samples_split: 2

min_samples_leaf: 1

🔹 4. Model Evaluation
Evaluated using:

Accuracy

Precision

Recall

F1-Score

📊 Dataset
Source: Kaggle – Loan Eligibility Prediction Dataset

Size: 614 rows × 13 features

Features include:
Loan amount, interest rate, credit score, employment history, income, etc.

🗂️ Project Structure

loan-eligibility-prediction/
│
├── app/ # Flask application
│ ├── templates/ # HTML templates
│ │ ├── home.html
│ │ └── index.html
│ └── static/ # Static files (CSS, JS, images)
│
├── src/ # Source code
│ ├── components/
│ │ └── model_trainer.py # ML model training
│ ├── exception/
│ │ └── CustomException.py
│ ├── logger/
│ │ └── logging.py
│ ├── pipeline/
│ │ └── predict_pipeline.py
│ └── utils/
│ └── utils.py
│
├── app.py # Main Flask application
├── Procfile # For deployment on Heroku/Render
├── requirements.txt # Dependencies
└── README.md # Project documentation

🌐 Live Demo
Check out the deployed version here:
👉 Live Demo on Render

https://loan-eligibility-prediction-system.onrender.com/
