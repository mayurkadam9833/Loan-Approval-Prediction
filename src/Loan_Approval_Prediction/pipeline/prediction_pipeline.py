import joblib
import pandas as pd 
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.gender_encoder=joblib.load(Path("artifacts/data_transformation/gender_encoder.joblib"))
        self.MaritalStatus_encoder=joblib.load(Path("artifacts/data_transformation/MaritalStatus_encoder.joblib"))
        self.Education_encode=joblib.load(Path("artifacts/data_transformation/Education_encode.joblib"))
        self.Employment_encode=joblib.load(Path("artifacts/data_transformation/Employment_encode.joblib"))
        self.Purpose_encode=joblib.load(Path("artifacts/data_transformation/Purpose_encode.joblib"))
        self.scale=joblib.load(Path("artifacts/data_transformation/scale.joblib"))
        self.model=joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    def preprocess(self,data:pd.DataFrame):
        data["Gender"]=data["Gender"].apply(self.gender_encoder.transform)
        data["MaritalStatus"]=data["MaritalStatus"].apply(self.MaritalStatus_encoder.transform)
        data=pd.concat([data.drop(["EducationLevel"],axis=1),pd.DataFrame(self.Education_encode.transform(data[["EducationLevel"]]),columns=self.Education_encode.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["EmploymentStatus"],axis=1),pd.DataFrame(self.Employment_encode.transform(data[["EmploymentStatus"]]),columns=self.Employment_encode.get_feature_names_out())],axis=1)
        data=pd.concat([data.drop(["PurposeOfLoan"],axis=1),pd.DataFrame(self.Purpose_encode.transform(data[["PurposeOfLoan"]]),columns=self.Purpose_encode.get_feature_names_out())],axis=1)
        data=self.scale.transform(data)
        return data 
    
    def prediction(self,data:pd.DataFrame):
        processed=self.preprocess(data)
        prediction=self.model.predict(processed)
        return prediction
    
