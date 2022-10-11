from V1.controllers.adminController import AdminController
from constants import httpError
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("AdminServices")


class AdminEventRouter:
    def getAllAdmin(self):
        try:
            result = AdminController().getAllAdmin()
            return result
        except Exception as e:
            logger.error("AdminEventRouter getAllAdmin() Exception : "+str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode,e.message,e.stack)

    def getAdmin(self,req):
        try:
            result = AdminController().getAdmin(req)
            return result
        except Exception as e:
            logger.error("AdminEventRouter getAdmin() Exception : "+str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode,e.message,e.stack)