import json

from V1.queries import userQuery, prenameQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("PrenameRepository")


class PrenameRepository:
    dbConnector = DBConnector()

    def getPrename(self):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(prenameQuery.FIND_ALL_PRENAMES)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("PrenameRepository getPrename() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()