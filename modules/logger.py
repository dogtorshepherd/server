import logging
import os
from datetime import datetime

from dotenv import load_dotenv

import log

load_dotenv()


class Logger:
    def __init__(self):
        self.logger = logging
        self.format = '[{name}][%(name)s][%(asctime)s][%(levelname)s]: %(message)s'.format(name=os.getenv("SYS_NAME"))
    def getLogger(self,name):
        formatter = logging.Formatter(self.format, datefmt='%Y-%m-%d %I:%M:%S')
        logging.basicConfig(level=logging.DEBUG, format=self.format,datefmt='%Y-%m-%d %H:%M:%S')
        now = datetime.now()
        dt_string = now.strftime("%Y_%m_%d_%H")
        directoryName = os.path.dirname(os.path.abspath(log.__file__))
        targetPath = os.path.join(directoryName,"Log",dt_string+".log")
        fh = logging.FileHandler(targetPath,encoding='utf-8')
        fh.setFormatter(formatter)
        self.logger = logging.getLogger(name)
        self.logger.addHandler(fh)
        return self.logger
