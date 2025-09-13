import os 
import yaml 
import json
from pathlib import Path
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox
from src.Loan_Approval_Prediction.logging import logger

# function to read yaml files
@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml,"r")as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file load sucessfully from path:{path_to_yaml}")
    
    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e 
    
    return ConfigBox(content)

# function to create directory
@ensure_annotations
def create_dir(file_path=list,verbose=True):
    for path in file_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("file directory create sucessfully")

# function to get size of file
@ensure_annotations 
def get_size(file):
    size_in_kb=round(os.path.getsize(file)/1024)
    return f"file size: {size_in_kb} KB"

# funstion to file in json format
@ensure_annotations 
def save_json(path:Path,data=dict):
    with open(path,"w")as file:
        json.dump(data,file,indent=4)
        logger.info(f"json file saved at path: {Path}")

