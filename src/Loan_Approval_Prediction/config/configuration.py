from src.Loan_Approval_Prediction.constants import *
from src.Loan_Approval_Prediction.utils.common import read_yaml,create_dir
from src.Loan_Approval_Prediction.entity.config_entity import DataIngestionConfig

"""
ConfigManager class is responsible for reading config, schema and params yaml files
and returning dataclass objects for each pipeline stage (ingestion, validation, transformation, training, evaluation)
"""
class ConfigManager:
    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        schema_file_path=SCHEMA_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH):

        # read all yaml files (config, schema, params)
        self.config=read_yaml(config_file_path)
        self.schema=read_yaml(SCHEMA_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)

        # create root artifact directory if not exists
        create_dir([self.config.artifacts_root])

    # method to get data ingestion config object
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        # create ingestion folder
        create_dir([config.root_dir])

        # prepare and return DataIngestionConfig dataclass
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir)
        
        return data_ingestion_config
        