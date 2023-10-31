import sys
import logging

#Exceptions - a type of error that occurs when a syntactically correct Python code raises an error
#sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()   #indicates which file and line the error is from
    
    #Creating variables that will be used in the format() function
    file_name =exc_tb.tb_frame.f_code.co_filename                 #to be able to fetch the file name, present under custom exception handling documentation in Python
        
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)   
        
    )
    return error_message


#Creating a user defined class
    
class CustomException(Exception): # The class inherits the parent exception that was defined in the function above
    def __init__(self, error_message, error_detail:sys ):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail= error_detail)
        
    def __str__(self):
        return self.error_message
    
    
#To check if the logger.py file is working
if __name__ =="main":
    
    try:
        a = 1/0
    except Exception as e:
        logging.info('Divide by zero error')
        raise CustomException(e,sys)
