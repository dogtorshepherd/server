import json

from V1.services.courseService import CourseService
from V1.services.majorService import MajorService
from V1.services.prenameService import PrenameService
from V1.services.userService import UserService
from constants import httpError
from models.ErrorModel import SystemErrorModel, ClientErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("CourseController")


class CourseController:
    def getCourse(self):
        try:
            data = CourseService().getCourse()
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("CourseController getCourse Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)