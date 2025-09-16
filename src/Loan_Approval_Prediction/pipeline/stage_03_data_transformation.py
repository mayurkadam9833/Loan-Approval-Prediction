from src.Loan_Approval_Prediction.config.configuration import ConfigManager
from src.Loan_Approval_Prediction.components.data_transformation import DataTransformation



class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.data_preprocessing()
        data_transformation.label_encode()
        data_transformation.scale_and_split()

        
        
