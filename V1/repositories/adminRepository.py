import json

from V1.queries import adminQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

log = Logger()
logger = log.getLogger("AdminRepository")


class AdminRepository:
    dbConnector = DBConnector()

    def findAllAdminData(self):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(adminQuery.FIND_ALL_ADMIN)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("AdminRepository findAllAdminData() Exception: "+json.dumps(e.__dict__))
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e)
            raise SystemErrorModel(e.statusCode,e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.dbConnector.close()

    def findAdminDataByParams(self,whereClause,params):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(adminQuery.FIND_ADMIN_WHERE_CLAUSE(whereClause),params)

            return self.cursor.fetchall()
        except Exception as e:
            logger.error("AdminRepository findAdminDataByParams() Exception: " +json.dumps(e.__dict__))
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.dbConnector.close()

    def insertAdmin(self,userId,adminId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(adminQuery.INSERT_ADMIN,(userId,adminId))
            return True
        except Exception as e:
            logger.error("AdminRepository insertAdmin() Exception: "+json.dumps(e.__dict__))
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.dbConnector.close()

    def editAdmin(self,userId,adminId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(adminQuery.EDIT_ADMIN,(adminId,userId))
            return True
        except Exception as e:
            logger.error("AdminRepository insertAdmin() Exception: "+json.dumps(e.__dict__))
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.dbConnector.close()

    # def updateAdmin(self,userId,enable):
    #     try:
    #         self.con = self.dbConnector.connect()
    #         self.cursor = self.dbConnector.getCursor()
    #         self.cursor.execute(adminQuery.UPDATE_ADMIN,(enable,userId))
    #         return True
    #     except Exception as e:
    #         logger.error("AdminRepository updateAdmin() Exception: "+json.dumps(e.__dict__))
    #         if not hasattr(e, 'httpCode'):
    #             raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
    #         raise SystemErrorModel(e.statusCode, e.message, e.stack)
    #     finally:
    #         self.con.commit()
    #         self.cursor.close()
    #         self.dbConnector.close()


