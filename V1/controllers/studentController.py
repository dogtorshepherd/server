import json

from V1.services.studentService import StudentService
from V1.services.teacherService import TeacherService
from V1.services.userService import UserService
from constants import httpError
from models.ErrorModel import SystemErrorModel, ClientErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("StudentController")


class StudentController:
    def getSubjects(self,params):
        try:
            groupId = ""
            if 'group_id' in params:
                groupId = params['group_id']
            data = StudentService().getStudentOnGroup(groupId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("StudentController getSubjects Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def getStudent(self,params):
        try:
            userId = ""
            studentId = ""
            search = ""

            if "user_id" in params :
                userId = params['user_id']
            if "student_id" in params:
                studentId = params['student_id']
            if "search" in params:
                search = params['search']
            data = StudentService().getStudentAll(userId, studentId, search)


            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("StudentController getStudent Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
