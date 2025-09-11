import os 
import logging 
from pathlib import Path 

# config logging format
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

# define project name
project_name="Loan_Approval_Prediction"

# list of files required for project with directories
list_of_files=[
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "schema.yaml", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"]

# loop through each file path to create directories and files if not exists 
for filepath in list_of_files:
    filepath=Path(filepath)
    file_dir,file_name=os.path.split(filepath)  # split file directory and filename

    # create file directory if not exists
    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)     
        logging.info(f"creating {file_dir} for {file_name}") 
    
    # create file if not exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w")as f:
            pass 
        logging.info(f"creating empty {file_name}")
    
    # return if file is already exits
    else:
        logging.info(f"{file_name} is already exists")



