import os 
import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from src.Loan_Approval_Prediction.utils.common import save_json
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score,roc_auc_score
from src.Loan_Approval_Prediction.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config
    
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
            model=joblib.load(self.config.model_path)
            
            test_x=data.drop([self.config.target_col],axis=1)
            test_y=data[self.config.target_col]

            prediction=model.predict(test_x)

            (acc,cf,pr,rc,f1,roc)=self.get_metrics(test_y,prediction)

            metrics={"accuracy score":acc,"confusion matrix":cf.tolist(),"precision score":pr,"recall score":rc,"f1-score":f1,"roc auc score":roc}

            save_json(Path(self.config.evaluation_file),metrics)
        
        except Exception as e:
            raise e
