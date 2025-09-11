import os
import zipfile
from urllib.request import urlretrieve
from src.Loan_Approval_Prediction.entity.config_entity import DataIngestionConfig
from src.Loan_Approval_Prediction.utils.common import get_size
from src.Loan_Approval_Prediction.logging import logger


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config 
    # method to download dataset from url
    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                # download file from source_url and save to local_data_file
                filename,header=urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.local_data_file
                )
                logger.info(f"file download completed from following header:\n{header}")
            
            else:
                # if file already exists, log the size of the file
                logger.info(f"file is already exists of size: {get_size(self.config.local_data_file)}")
        
        except Exception as e:
            raise e 
    
    # method to unzip dataset
    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)  # create folder if not exists
        with zipfile.ZipFile(self.config.local_data_file,"r")as zipref:
            zipref.extractall(unzip_path)      # extract all files inside unzip_dir
            logger.info(f"file extraction completed")

