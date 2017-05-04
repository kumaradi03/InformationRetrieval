from traceback import format_exc
from path_define import get_ERROR_FILE_PATH

ERROR_FILE_PATH=get_ERROR_FILE_PATH()

def logerror(e):
    ERROR_FILE=open(ERROR_FILE_PATH,'a')
    ERROR_FILE.write(format_exc())
    ERROR_FILE.close()
