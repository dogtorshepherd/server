from V1.controllers.studentController import StudentController
from V1.controllers.teacherController import TeacherController
from V1.controllers.userController import UserController
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("StudentEventRouter")


class StudentEventRouter:
    def getStudent(self,params):
        try:
            result = StudentController().getSubjects(params)
            return result
        except Exception as e:
            logger.error("StudentEventRouter getStudent() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def getStudentAll(self,params):
        try:
            result = StudentController().getStudent(params)
            return result
        except Exception as e:
            logger.error("StudentEventRouter getStudentAll() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)