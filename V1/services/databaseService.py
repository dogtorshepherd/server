import json

from V1.repositories.databaseRepository import DatabaseRepository
from V1.utils.transformUtils import TransformUtils
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

logger = Logger().getLogger("DatabaseService")


class DatabaseService:

    def getDatabase(self):
        try:
            databaseRepo = DatabaseRepository()
            result = databaseRepo.getDatabase()
            resultList = []
            for item in result:
                resultList.append(item)

            return resultList
        except Exception as e:
            logger.error("DatabaseService getDatabase() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def getDatabaseInfo(self, databaseId):
        try:
            databaseRepo = DatabaseRepository()
            whereClause = " AND d.database_id=%s"
            params = (databaseId,)
            result = databaseRepo.getDatabaseInfo(whereClause, params)
            return result
        except Exception as e:
            logger.error("DatabaseService getDatabaseInfo() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def addDatabase(self, databaseName, script):
        try:
            databaseRepo = DatabaseRepository()
            params = (databaseName,)
            databaseRepo.runScript(script="CREATE DATABASE {dbName}".format(dbName=databaseName))
            result = databaseRepo.addDatabase(params)

            if result:
                databaseRepo.runScript(databaseName,script);
            return {'databaseId': result}
        except Exception as e:
            logger.error("DatabaseService addDatabase() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)