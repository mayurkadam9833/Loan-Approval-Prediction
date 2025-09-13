from pathlib import Path 
from dataclasses import dataclass 

# Configuration dataclass for data ingestion process (directories, file paths, and source URL)
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str 
    local_data_file: Path 
    unzip_dir: Path

# Configuration dataclass for data validation process (directories, file paths)
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    unzip_data: Path 
    STATUS_FILE: str
    all_schema: dict

# Configuration dataclass for data transformation process (directories, file paths)
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path 
    data_path: Path
    traget_column: str

# Configuration dataclass for model trainer process (directories, file paths,model parameters)
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path 
    train_data_path: Path
    model_name: str
    criterion: str
    max_depth: int 
    max_samples: int
    min_samples_leaf: int 
    min_samples_split: int
    n_estimators: int
    target_col: str

# Configuration dataclass for model evaluation process (directories, file paths)
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    evaluation_file: Path
    target_col: str

