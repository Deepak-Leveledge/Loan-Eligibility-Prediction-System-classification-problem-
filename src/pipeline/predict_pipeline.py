import sys 
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utlis import load_object
import numpy as np


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path="artifacts/model.pkl"
            preprocessor_path="artifacts/preprocessor.pkl"
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)

            data_scaled=preprocessor.transform(features)
            pred=model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e,sys)
        


class CustomData:
    def __init__(self,
                Married: str,
                Education: str,
                Self_Employed: str,
                ApplicantIncome: float,
                LoanAmount: float,
                Credit_History: float,
                Property_Area: str):
        
        self.Married = Married
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.ApplicantIncome = ApplicantIncome
        self.LoanAmount = LoanAmount
        self.Credit_History = Credit_History
        self.Property_Area = Property_Area

    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Married": [self.Married],
                "Education": [self.Education],
                "Self_Employed": [self.Self_Employed],
                "ApplicantIncome": [self.ApplicantIncome],
                "LoanAmount": [self.LoanAmount],
                "Credit_History": [self.Credit_History],
                "Property_Area": [self.Property_Area]
            }


            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)

