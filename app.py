import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData ,PredictPipeline

application = Flask(__name__)

app= application
# model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loanpredict',methods=['GET','POST'])
def loanpredict():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Married=request.form.get('Married'),
            Education=request.form.get('Education'),
            Self_Employed=request.form.get('Self_Employed'),
            ApplicantIncome = float(request.form.get('ApplicantIncome').split('-')[0]),
            LoanAmount=float(request.form.get('LoanAmount')),
            Credit_History=float(request.form.get('Credit_History')),
            Property_Area=request.form.get('Property_Area')
        )
        final_new_data=data.get_data_as_data_frame()
        print(final_new_data)
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        if pred==0:
            return render_template('home.html',prediction_text="Loan is not approved")
        else:
            return render_template('home.html',prediction_text="Loan is approved")

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)