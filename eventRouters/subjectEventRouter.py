from V1.controllers.subjectController import SubjectController
from V1.controllers.teacherController import TeacherController
from V1.controllers.userController import UserController
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

log = Logger()
logger = log.getLogger("SubjectEventRouter")


class SubjectEventRouter:
    def getSubjects(self,params):
        try:
            result = SubjectController().getSubjects(params)
            return result
        except Exception as e:
            logger.error("SubjectEventRouter getSubjects() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createSubjects(self,body):
        try:
            result = SubjectController().createSubjects(body)
            return result
        except Exception as e:
            logger.error("SubjectEventRouter createSubjects() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def editSubject(self,body):
        try:
            result = SubjectController().editSubject(body)
            return result
        except Exception as e:
            logger.error("SubjectEventRouter editSubject() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteSubject(self,params):
        try:
            result = SubjectController().deleteSubject(params)
            return result
        except Exception as e:
            logger.error("SubjectEventRouter deleteSubject() Exception : " + str(e))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, e.__str__())
            raise SystemErrorModel(e.statusCode, e.message, e.stack)