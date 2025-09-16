import joblib
import pandas as pd 
import numpy as np
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.encode_education=joblib.load(Path("artifacts/data_transformation/encode_education.joblib"))
        self.encode_self_employed=joblib.load(Path("artifacts/data_transformation/encode_self_employed.joblib"))
        self.scale=joblib.load(Path("artifacts/data_transformation/scale.joblib"))
        self.model=joblib.load(Path("artifacts/model_trainer/model.joblib"))
    
    def preprocess(self,data:pd.DataFrame):
        data["education"]=self.encode_education.transform(data["education"])
        data["self_employed"]=self.encode_self_employed.transform(data["self_employed"])
        data=self.scale.transform(data)
        return data 
    
    def prediction(self,data:pd.DataFrame):
        processed=self.preprocess(data)
        prediction=self.model.predict(processed)
        return prediction
    
