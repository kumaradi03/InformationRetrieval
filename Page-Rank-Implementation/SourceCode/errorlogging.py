from traceback import format_exc

ERROR_FILE_PATH="errorLog.txt"

def logerror(e):
    ERROR_FILE=open(ERROR_FILE_PATH,'a')
    ERROR_FILE.write(format_exc())
    ERROR_FILE.close()
