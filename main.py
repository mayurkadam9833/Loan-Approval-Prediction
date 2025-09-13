from src.Loan_Approval_Prediction.logging import logger
from src.Loan_Approval_Prediction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.Loan_Approval_Prediction.pipeline.stage_02_data_validation import DataValidationPipeline
from src.Loan_Approval_Prediction.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.Loan_Approval_Prediction.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.Loan_Approval_Prediction.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
# data ingestion pipeline [download data from source url and extract to defined path] 
stage_one="Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_one} started >>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_one} completed >>>>")
    
    except Exception as e:
        logger.info(e)
        raise e

# data validation pipeline [schema validation] 
stage_two="Data Validation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_two} started >>>>")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_two} completed >>>>")
    
    except Exception as e:
        logger.info(e)
        raise e

# data tarnsformation pipeline [data preprocessing,encoding,scaling,oversampling,train and test split] 
stage_three="Data Transformation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_three} started >>>>")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_three} completed >>>>")
    
    except Exception as e:
        logger.info(e)
        raise e


stage_four="Model trainer"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_four} started >>>>")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_four} completed >>>>")
    
    except Exception as e:
        logger.info(e)
        raise e

stage_five="Model Evaluation"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage:{stage_five} started >>>>")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"<<<< stage:{stage_five} completed >>>>")
    
    except Exception as e:
        logger.info(e)
        raise e

