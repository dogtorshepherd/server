import json

from V1.repositories.adminRepository import AdminRepository
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("AdminServices")


class AdminServices:
    def getAllAdmin(self):
        try:
            adminRepo = AdminRepository()
            result = adminRepo.findAllAdminData()
            print(result)
            return result
        except Exception as e:
            logger.error("AdminServices getAllAdmin() Exception: "+ json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)

    def getAdmin(self,adminId,username):
        try:
            adminRepo = AdminRepository()
            whereClause = ""
            params = ()
            if adminId :
                whereClause += " AND u.user_id = %s"
                params += params + (adminId,)
            if username :
                whereClause += " AND u.user_username = %s"
                params += params + (username,)
            result = adminRepo.findAdminDataByParams(whereClause,params)
            res = []
            for row in result:
                res.append(row)
            return res
        except Exception as e:
            logger.error("AdminServices getAdmin() Exception: "+ json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            raise SystemErrorModel(e.statusCode, e.message,e.stack)