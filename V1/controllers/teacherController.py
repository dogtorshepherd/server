import json

from V1.services.teacherService import TeacherService
from V1.services.userService import UserService
from constants import httpError
from models.ErrorModel import SystemErrorModel, ClientErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("TeacherController")


class TeacherController:
    def getTeachers(self,params):
        try:
            teacherId =""
            if 'teacherId' in params:
                teacherId = params['teacherId']

            data = TeacherService().getTeachers(teacherId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("TeacherController getTeachers Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
