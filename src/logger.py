#The purpose of this file is to ensure that information on execution in files is saved. Basically, leeping track of logs

import logging
import os
from datetime import datetime

#Definition of how the log file will be created
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path =os.path.join(os.getcwd(),"logs",LOG_FILE) #cwd -current working directory
os.makedirs(logs_path, exist_ok =True) #Even if there is an existing folder, keep on updating and creating the log files

LOG_FILE_PATH =os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename =LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level =logging.INFO,
)
 
#To check if the logger.py file is working
if __name__ =="main":
    logging.info("Logging has started")