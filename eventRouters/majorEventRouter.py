from V1.controllers.majorController import MajorController
from V1.controllers.prenameController import PrenameController
from V1.controllers.userController import UserController
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("MajorEventRouter")


class MajorEventRouter:
    def getMajorEventRouter(self):
        try:
            result = MajorController().getMajor()
            return result
        except Exception as e:
            logger.error("MajorEventRouter getMajorEventRouter() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

