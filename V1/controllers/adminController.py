from V1.services.adminServices import AdminServices
from constants import httpError
from models.ErrorModel import SystemErrorModel
from models.ResponseBasic import ResponseSuccessWithData
from modules.logger import Logger

log = Logger()
logger = log.getLogger("AdminController")


class AdminController:
    def getAllAdmin(self):
        try:
            result = AdminServices().getAllAdmin()
            return ResponseSuccessWithData(result)
        except Exception as e:
            logger.error("AdminController getAllAdmin() Exception: " + str(e))
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)

    def getAdmin(self,req):
        try:
            adminId = None
            username = None
            if "admin_id" in req:
                adminId = req["admin_id"]
            if "username" in req:
                username = req["username"]
            result = AdminServices().getAdmin(adminId,username)
            return ResponseSuccessWithData(result)
        except Exception as e:
            logger.error("AdminController getAdmin() Exception: " + str(e))
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)