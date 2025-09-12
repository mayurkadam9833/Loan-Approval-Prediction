from src.Loan_Approval_Prediction.config.configuration import ConfigManager
from src.Loan_Approval_Prediction.components.data_validation import DataValidation



"""
DataValidationPipeline class is pipeline to validation of dataset schema
"""
class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()

