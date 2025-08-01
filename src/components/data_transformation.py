import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
import numpy as np


from dataclasses import dataclass
from src.utlis import save_object


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    def get_data_transformer_object(slef):
        try:
            logging.info("Data Transformation Initiated")

            numerical_columns=['ApplicantIncome','LoanAmount','Credit_History']
            categorical_columns=['Married','Education','Self_Employed','Property_Area']


            num_pipleline=Pipeline([
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
            ])


            cat_pipleline=Pipeline([
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False))
            ])


            # logging.info("Numerical columns standard scaling completed")

            # preprocessor=ColumnTransformer([
            #     ('num_pipeline',num_pipleline,numerical_features),
            #     ('cat_pipleline',cat_pipleline,categorical_features)
            # ])


            logging.info(f"Numerical Columns{str(numerical_columns)}")
            logging.info(f"Categorical Columns{str(categorical_columns)}")


            # logging.info(f"Numerical Columns",{numerical_columns})
            # logging.info(f"Categorical Columns",{categorical_columns})





            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipleline,numerical_columns),
                ('cat_pipleline',cat_pipleline,categorical_columns)
            ])


            return preprocessor

            

            
        except Exception as e:
            raise CustomException(e,sys)    
        

    def initate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name='Loan_Status'
            train_df[target_column_name] = train_df[target_column_name].map({'Y': 1, 'N': 0})
            test_df[target_column_name] = test_df[target_column_name].map({'Y': 1, 'N': 0})
            
            numerical_columns=['ApplicantIncome','LoanAmount','Credit_History']

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe"
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr=np.c_[
                input_feature_train_arr,
                np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,
                np.array(target_feature_test_df)
            ]

            logging.info(f"Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
            