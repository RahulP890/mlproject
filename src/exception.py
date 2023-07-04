import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name , line_number , error_msg = exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error)
    error_message="Error in Python Script [{0}] at line number [{1}] \n which says as :[{2}]".format(file_name,line_number,error_msg)
    return error_message
    
class CustomeException(Exception):
    def __init__(self, error_message,error_detail:sys) :
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        error=1/0
    except Exception as err:
        logging.info("Costomized Error in Action")
        raise CustomeException(err,sys)