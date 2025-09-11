import os 
import sys
import logging

# Define logging format (timestamp : loglevel module message)
log_str="[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

# Get current directory path where this file is located
curr_dir=os.path.abspath(os.path.dirname(__file__))

# Define log folder and log file path
log_dir=os.path.join(curr_dir,"logs")
log_path=os.path.join(log_dir,"runnings_logs.log")

# Create log directory if it doesn't exist
os.makedirs(log_dir,exist_ok=True)

# Configure logging to write logs to both file and console
logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger object for the project
logger=logging.getLogger("Loan_approval_prediction")