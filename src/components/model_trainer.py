import os 
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.ensemble import(
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier
)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.metrics import r2_score

from src.utlis import save_object
from src.utlis import evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
        

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Splitting Dependent and Independent variables from train and test data")
            
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )


            ## models initialization
            models={
                "Random Forest":RandomForestClassifier(),
                "Decision Tree":DecisionTreeClassifier(),
                "Gradient Boosting":GradientBoostingClassifier(),
                "XGBClassifier":XGBClassifier(),
                "CatBoosting Classifier":CatBoostClassifier(verbose=False),
                "AdaBoost Classifier":AdaBoostClassifier()
            }


            params={
                "Random Forest":{
                    'criterion':['gini', 'entropy', 'log_loss'],
                    # 'max_features':['sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Decision Tree":{
                      'criterion': ['gini', 'entropy', 'log_loss'],
                      'min_samples_split': [2, 5, 10],
                      'min_samples_leaf': [1, 2, 4],
                      'max_features': ['auto', 'sqrt', 'log2']
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.9],
                    'criterion':['friedman_mse','squared_error'],
                    'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "XGBClassifier":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Classifier":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Classifier":{
                    'learning_rate':[.1,.01,0.5,.001],
                    'n_estimators': [8,16,32,64,128,256]
                }
            }



            model_report:dict=evaluate_models(X_train,y_train,X_test,y_test,models,params)

            ## To get the best model score from dict 
            best_model_score=max(sorted(model_report.values()))

            ## To get the best model name from dict

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            print(f"Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}")
            print("\n====================================================================================\n")
            logging.info(f"Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted=best_model.predict(X_test)

            r2_square=r2_score(y_test,predicted)

            return r2_square
        except Exception as e:
            raise CustomException(e,sys)