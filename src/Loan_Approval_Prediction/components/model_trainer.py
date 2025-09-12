import os
import pandas as pd 
import joblib
from sklearn.ensemble import RandomForestClassifier
from src.Loan_Approval_Prediction.entity.config_entity import ModelTrainerConfig
from src.Loan_Approval_Prediction.logging import logger

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config
        self.model=RandomForestClassifier(criterion=self.config.criterion,max_depth=self.config.max_depth,max_samples=self.config.max_samples,min_samples_leaf=self.config.min_samples_leaf,min_samples_split=self.config.min_samples_split,n_estimators=self.config.n_estimators)


    def train_model(self):
        try:
            data=pd.read_csv(self.config.train_data_path)

            train_x=data.drop([self.config.target_col],axis=1)
            train_y=data[self.config.target_col]

            model=self.model.fit(train_x,train_y)

            model_path=os.path.join(self.config.root_dir,self.config.model_name)
            joblib.dump(model,model_path)

            logger.info(f"Model trained sucessfully and saved")

        except Exception as e:
            raise e

            





        