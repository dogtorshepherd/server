import os
from dotenv import load_dotenv
import mysql.connector
from mysqlx import errorcode

from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("DBConnector")
load_dotenv()


class DBConnector:
    def __init__(self, dbname="flask_api_db"):
        self.dbname = dbname
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.port = os.getenv('DB_PORT')
        self.host = os.getenv('DB_HOST')

    def connect(self,dbname="flask_api_db"):
        try:
            if dbname:
                self.dbname = dbname
            self.con = mysql.connector.connect(user=self.user, password=self.password,database=self.dbname,port=self.port,host=self.host)
            return self.con
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("Something is wrong with your user name or password")
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("Database does not exist")
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            else:
                logger.error(str(err.__dict__))
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)

    def getCursor(self):
        try:
            self.cursor = self.con.cursor(buffered=True,dictionary=True)
            return self.cursor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("Something is wrong with your user name or password")
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("Database does not exist")
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            else:
                logger.error(str(err.__dict__))
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)

    def close(self):
        try:
            self.con.close()
            logger.debug("Connection Close")
        except mysql.connector.Error as err:
            logger.error(str(err.__dict__))
            raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE,httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
