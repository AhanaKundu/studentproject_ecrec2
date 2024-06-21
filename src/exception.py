import sys
import logging 
def error_msg_detail(error, error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message= "error occured in python script name [{0}] line no. [{1}] error: [{2}]".format(file_name, exc_tb.tb_lineno, str(error))
    return (error_message)

class customException(Exception):
    def  __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message= error_msg_detail(error_message, error_detail=error_detail) # type: ignore
    
    def __str__(self):
         return self.error_message
    
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as E:
#         logging.info("devidebyzeroerror")
#         raise customException(E, sys)
    