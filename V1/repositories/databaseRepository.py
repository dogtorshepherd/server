import json

from V1.queries import userQuery, prenameQuery, majorQuery, databaseQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("DatabaseRepository")


class DatabaseRepository:
    dbConnector = DBConnector()

    def getDatabase(self):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(databaseQuery.FIND_ALL_DATABASE)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("DatabaseRepository getDatabase() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def getDatabaseInfo(self,whereclause='',params = ()):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(databaseQuery.FIND_INFO_DATABASE(whereclause), params)
            return self.cursor.fetchone()
        except Exception as e:
            logger.error("DatabaseRepository getDatabaseInfo() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def addDatabase(self,params = ()):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(databaseQuery.INSERT_DATABASE, params)
            databaseId = self.cursor.lastrowid
            return databaseId
        except Exception as e:
            logger.error("DatabaseRepository addDatabase() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def runScript(self,databaseName="flask_api_db",script=""):
        try:
            self.con = self.dbConnector.connect(databaseName)
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(script)
            return True
        except Exception as e:
            logger.error("DatabaseRepository runScript() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()