import os 
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from src.Loan_Approval_Prediction.utils.common import save_json
from src.Loan_Approval_Prediction.logging import logger
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,roc_auc_score
from src.Loan_Approval_Prediction.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
        self.model=joblib.load(self.config.model_path)
    
    def get_metrics(self,actual,predicted):
        acc=accuracy_score(actual,predicted)
        cf=confusion_matrix(actual,predicted)
        pr=precision_score(actual,predicted)
        rc=recall_score(actual,predicted)
        f1=f1_score(actual,predicted)
        roc=roc_auc_score(actual,predicted)
        return acc,cf,pr,rc,f1,roc
    
    def evaluation(self):
        try:
            data=pd.read_csv(self.config.test_data_path)
            
            test_x=data.drop([self.config.target_col],axis=1)
            test_y=data[[self.config.target_col]]

            pred=self.model.predict(test_x)

            (acc_test,cf_test,pr_test,rc_test,f1_test,roc_test)=self.get_metrics(test_y,pred)

            metrics={"accuracy score":acc_test,"confusion matrix":cf_test.tolist(),"precision score":pr_test,"recall score":rc_test,"f1-score":f1_test,"roc auc score":roc_test}

            save_json(Path(self.config.evaluation_file),metrics)
        
        except Exception as e:
            raise e
