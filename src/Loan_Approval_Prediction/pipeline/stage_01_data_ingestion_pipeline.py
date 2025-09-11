from src.Loan_Approval_Prediction.logging import logger
from src.Loan_Approval_Prediction.config.configuration import ConfigManager
from src.Loan_Approval_Prediction.components.data_ingestion import DataIngestion

"""
DataIngestionPipeline class is pipeline to download file and extract file in define folder
"""
class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_file()
