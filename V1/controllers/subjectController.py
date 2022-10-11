import json

from V1.services.subjectService import SubjectService
from V1.services.teacherService import TeacherService
from V1.services.userService import UserService
from constants import httpError
from models.ErrorModel import SystemErrorModel, ClientErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("SubjectController")


class SubjectController:
    def getSubjects(self,params):
        try:
            subjectId =""
            if 'subjectId' in params:
                subjectId = params['subjectId']
            data = SubjectService().getSubject(subjectId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("SubjectController getSubjects Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createSubjects(self, body):
        try:
            subject_code = body['subject_code']
            subject_name = body['subject_name']
            subject_decription = body['subject_decription']
            course_name = body['course_name']
            subject_year = body['subject_year']
            course_id = body['course_id']
            group = body['group']
            enable = body['enable']

            data = SubjectService().createSubject(subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("SubjectController createSubject Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def editSubject(self, body):
        try:
            subject_id = body['subject_id']
            subject_code = body['subject_code']
            subject_name = body['subject_name']
            subject_decription = body['subject_decription']
            course_name = body['course_name']
            subject_year = body['subject_year']
            course_id = body['course_id']
            group = body['group']
            enable = body['enable']

            data = SubjectService().editSubject(subject_id, subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("SubjectController editSubject Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteSubject(self, params):
        try:
            subjectId =""
            if 'subjectId' in params:
                subjectId = params['subjectId']
            data = SubjectService().deleteSubject(subjectId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("SubjectController deleteSubject Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)