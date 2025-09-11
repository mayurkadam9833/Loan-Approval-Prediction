from pathlib import Path 
from dataclasses import dataclass 

# Configuration dataclass for data ingestion process (directories, file paths, and source URL)
dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str 
    local_data_file: Path 
    unzip_dir: Path