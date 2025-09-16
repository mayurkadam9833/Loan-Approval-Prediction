import os
import joblib
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler 
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from src.Loan_Approval_Prediction.logging import logger
from src.Loan_Approval_Prediction.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config 
        self.encode_education=LabelEncoder()
        self.encode_self_employed=LabelEncoder()
        self.encode_loan_status=LabelEncoder()
        self.scale=StandardScaler()
        self.sampling=SMOTE()
        
    def data_preprocessing(self):
        data=pd.read_csv(self.config.data_path)
        data=data.drop(["loan_id"],axis=1)

        new_cols = []
        for col in data.columns:
            new_cols.append(col.strip())   # remove spaces
        data.columns = new_cols
        return data 
    
    def label_encode(self):
        data=self.data_preprocessing()
        data["education"]=self.encode_education.fit_transform(data["education"])
        data["self_employed"]=self.encode_self_employed.fit_transform(data["self_employed"])
        data["loan_status"]=self.encode_loan_status.fit_transform(data["loan_status"])

        joblib.dump(self.encode_education,os.path.join(self.config.root_dir,"encode_education.joblib"))
        joblib.dump(self.encode_self_employed,os.path.join(self.config.root_dir,"encode_self_employed.joblib"))
        joblib.dump(self.encode_loan_status,os.path.join(self.config.root_dir,"encode_loan_status.joblib"))
        return data 
    
    
    def scale_and_split(self):
        try:
            data=self.label_encode()
            
            x=data.drop([self.config.target_col],axis=1)
            y=data[self.config.target_col]
            
            train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2)
            
            sampled_train_x,sampled_train_y=self.sampling.fit_resample(train_x,train_y)
            
            scale_train_x=self.scale.fit_transform(sampled_train_x)
            scale_test_x=self.scale.transform(test_x)

            joblib.dump(self.scale,os.path.join(self.config.root_dir,"scale.joblib"))

            train_data=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),sampled_train_y],axis=1)
            test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),pd.Series(test_y).reset_index(drop=True)],axis=1)
            
            train_data.to_csv(os.path.join(self.config.root_dir,"train_data.csv"),index=False)
            test_data.to_csv(os.path.join(self.config.root_dir,"test_data.csv"),index=False)

            logger.info(f"Data split sucessfully into train and test")
            logger.info("Train data shape:",train_data.shape)
            logger.info("Test data shape:",test_data.shape)
            

        except Exception as e:
            raise e 
        

        



        
            
            


            

