from V1.controllers.databaseController import DatabaseController
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("DatabaseEventRouter")


class DatabaseEventRouter:
    def getDatabaseEventRouter(self):
        try:
            result = DatabaseController().getDatabase()
            return result
        except Exception as e:
            logger.error("DatabaseEventRouter getDatabaseEventRouter() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)


    def getDatabaseInfoEventRouter(self, params):
        try:
            result = DatabaseController().getDatabaseInfo(params)
            return result
        except Exception as e:
            logger.error("DatabaseEventRouter getDatabaseInfoEventRouter() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def addDatabaseEventRouter(self, body):
        try:
            result = DatabaseController().addDatabase(body)
            return result
        except Exception as e:
            logger.error("DatabaseEventRouter getDatabaseInfoEventRouter() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
