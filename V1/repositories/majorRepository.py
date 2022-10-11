import json

from V1.queries import userQuery, prenameQuery, majorQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("MajorRepository")


class MajorRepository:
    dbConnector = DBConnector()

    def getMajor(self):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(majorQuery.FIND_ALL_MAJOR)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("MajorRepository getMajor() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()