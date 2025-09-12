import os
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler 
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from src.Loan_Approval_Prediction.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config 
        self.gender_encoder=LabelEncoder()
        self.MaritalStatus_encoder=LabelEncoder()
        self.LoanApproved_encoder=LabelEncoder()
        self.Education_encode=OneHotEncoder(sparse_output=False)
        self.Employment_encode=OneHotEncoder(sparse_output=False)
        self.Purpose_encode=OneHotEncoder(sparse_output=False)
        self.scale=StandardScaler()
        self.sampling=SMOTE()
        
    def data_preprocessing(self):
        data=pd.read_csv(self.config.data_path)
        data.drop(["CustomerID","Name"],axis=1,inplace=True)
        data["MaritalStatus"]=data["MaritalStatus"].replace({"Divorced":"Non-Married",
                                                     "Single":"Non-Married",
                                                     "Widowed":"Non-Married"})
        return data 
    
    def label_encode(self):
        data=self.data_preprocessing()
        data["Gender"]=data[["Gender"]].apply(self.gender_encoder.fit_transform)
        data["MaritalStatus"]=data[["MaritalStatus"]].apply(self.MaritalStatus_encoder.fit_transform)
        data["LoanApproved"]=data[["LoanApproved"]].apply(self.LoanApproved_encoder.fit_transform)
        return data 
    
    def ohe_encode(self):
        data=self.label_encode()
        data=pd.concat([data.drop(["EducationLevel"],axis=1),pd.DataFrame(self.Education_encode.fit_transform(data[["EducationLevel"]]),columns=self.Education_encode.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["EmploymentStatus"],axis=1),pd.DataFrame(self.Employment_encode.fit_transform(data[["EmploymentStatus"]]),columns=self.Employment_encode.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["PurposeOfLoan"],axis=1),pd.DataFrame(self.Purpose_encode.fit_transform(data[["PurposeOfLoan"]]),columns=self.Purpose_encode.get_feature_names_out())],axis=1)
        return data 
    
    def scale_and_split(self):
        try:
            data=self.ohe_encode()
            
            x=data.drop([self.config.traget_column],axis=1)
            y=data[[self.config.traget_column]]
            
            train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=42)
            
            sampled_train_x,sampled_train_y=self.sampling.fit_resample(train_x,train_y)
            
            scale_train_x=self.scale.fit_transform(sampled_train_x)
            scale_test_x=self.scale.transform(test_x)
            
            train_data=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),(sampled_train_y)],axis=1)
            test_data=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),test_y],axis=1)
            
            train_data.to_csv(os.path.join(self.config.root_dir,"train_data.csv"))
            test_data.to_csv(os.path.join(self.config.root_dir,"test_data.csv"))

        except Exception as e:
            raise e 
        

        



        
            
            


            

