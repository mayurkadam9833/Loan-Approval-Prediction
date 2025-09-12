from src.Loan_Approval_Prediction.constants import *
from src.Loan_Approval_Prediction.utils.common import read_yaml,create_dir
from src.Loan_Approval_Prediction.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig

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
        self.schema=read_yaml(schema_file_path)
        self.params=read_yaml(params_file_path)

        # create root artifact directory if not exists
        create_dir([self.config.artifacts_root])

    # method to get data ingestion config object
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        # create data ingestion folder
        create_dir([config.root_dir])

        # prepare and return DataIngestionConfig dataclass
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir)
        
        return data_ingestion_config
    
    # method to get data validation config object
    def get_data_validation_config(self)-> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        # create data validation folder
        create_dir([config.root_dir])

        # prepare and return DataValidationConfig dataclass
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data=config.unzip_data,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )
        return data_validation_config
    
    # method to get data transformation config object
    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation
        schema=self.schema.TARGET_COLUMN 

        # create data transformation folder
        create_dir([config.root_dir])

        # prepare and return DataTransformationConfig dataclass
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            traget_column=list(schema.keys())[0])

        return data_transformation_config