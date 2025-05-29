# -*- coding: utf-8 -*-
import os
import logging
from datetime import datetime

logging.basicConfig(filename='logger.txt',level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def file_lister(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for name in files:
                file_path = os.path.join(root, name)
                size = os.path.getsize(file_path)
                times = os.path.getmtime(file_path)
                mod_time = datetime.fromtimestamp(times).strftime('%Y-%m-%d %H:%M:%S')
                logging.info(f' - {name} - {size} - {mod_time}')


file_lister(
    r'C:\Users\Administrator\Desktop\Python资料及其他\Python_Study\StudyPython\Pyton之自动化脚本炼金术\batch_renamer\test')
