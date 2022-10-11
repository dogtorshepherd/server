from V1.controllers.teacherController import TeacherController
from V1.controllers.userController import UserController
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("TeacherEventRouter")


class TeacherEventRouter:
    def getTeachers(self,params):
        try:
            result = TeacherController().getTeachers(params)
            return result
        except Exception as e:
            logger.error("TeacherEventRouter getTeachers() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)