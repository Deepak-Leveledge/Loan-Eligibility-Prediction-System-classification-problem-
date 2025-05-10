## Loan Eligibility Prediction System ------> Calssification Problem

# Loan Eligibility Prediction System

Introduction
This project is a Loan Eligibility Prediction System built using Flask as the web framework and various machine learning libraries such as scikit-learn, catboost, and xgboost. The system aims to predict the eligibility of loan applicants based on their creditworthiness.

Model Used
The system uses a ensemble model that combines the predictions of three different models:

CatBoost Classifier: This model is used to handle categorical features and provides a good balance between accuracy and interpretability.
XGBoost Classifier: This model is used to handle numerical features and provides a good balance between accuracy and speed.
Random Forest Classifier: This model is used to handle both categorical and numerical features and provides a good balance between accuracy and interpretability.
Methods Used
The following methods were used to develop the system:

Data Preprocessing: The dataset was preprocessed to handle missing values, outliers, and feature scaling.
Feature Engineering: New features were engineered to improve the accuracy of the models.
Hyperparameter Tuning: Hyperparameter tuning was performed using GridSearchCV to optimize the performance of the models.
Model Evaluation: The models were evaluated using metrics such as accuracy, precision, recall, and F1-score.
Hyperparameter Tuning
The following hyperparameters were tuned for each model:

CatBoost Classifier:
iterations: 1000
learning_rate: 0.01
depth: 6
l2_leaf_reg: 3
XGBoost Classifier:
max_depth: 6
learning_rate: 0.01
n_estimators: 1000
gamma: 0.1
Random Forest Classifier:
n_estimators: 1000
max_depth: 6
min_samples_split: 2
min_samples_leaf: 1
Dataset Used
The dataset used for this project is the Loan Eligibility Prediction Dataset from Kaggle. The dataset contains 614 rows and 13 columns, including features such as loan amount, interest rate, credit score, and employment history.

Folder Structure
The project follows the following folder structure:

app: This folder contains the Flask application code.
app.py: The main application file.
templates: This folder contains the HTML templates for the application.
home.html: The home page template.
index.html: The index page template.
static: This folder contains the static files for the application.
src: This folder contains the source code for the project.
components: This folder contains the components used in the project.
model_trainer.py: The model trainer component.
exception: This folder contains the exception handling code.
CustomException.py: The custom exception class.
logger: This folder contains the logging code.
logging.py: The logging configuration file.
pipeline: This folder contains the data pipeline code.
predict_pipeline.py: The prediction pipeline component.
utils: This folder contains the utility functions.
utils.py: The utility functions file.
Procfile: The Procfile for the application.
README.md: This file.
Live Demo
A live demo of the system can be accessed at: https://loan-eligibility-prediction-system.onrender.com/

Future Work
Model Improvement: The models can be further improved by using techniques such as feature selection, dimensionality reduction, and ensemble methods.
Data Collection: More data can be collected to improve the accuracy of the models.
Deployment: The system can be deployed on a cloud platform to make it more accessible.
