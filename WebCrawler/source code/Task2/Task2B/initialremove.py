import os
from os.path import exists
from glob import glob
import path_define

CRAWLEDLISTPATH= path_define.get_CRAWLEDLISTPATH()+"\crawled_list.txt"
ERROR_FILE_PATH= path_define.get_ERROR_FILE_PATH()
CRAWLED_HTML_PATH = path_define.get_CRAWLED_HTML_PATH()

def remove_files():
    files=glob(CRAWLED_HTML_PATH+'\*.html')
    for filename in files:
        os.remove(filename)
    if exists(CRAWLEDLISTPATH):
        os.remove(CRAWLEDLISTPATH)
    if exists(ERROR_FILE_PATH):
        os.remove(ERROR_FILE_PATH)
