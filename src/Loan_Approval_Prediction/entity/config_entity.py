from pathlib import Path 
from dataclasses import dataclass 

# Configuration dataclass for data ingestion process (directories, file paths, and source URL)
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str 
    local_data_file: Path 
    unzip_dir: Path

# Configuration dataclass for data validation process (directories, file paths, and source URL)
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    unzip_data: Path 
    STATUS_FILE: str
