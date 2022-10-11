import json

from V1.queries import userQuery
from V1.repositories.subjectRepository import SubjectRepository
from V1.repositories.teacherRepository import TeacherRepository
from V1.repositories.userRepository import UserRepository
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("SubjectService")


class SubjectService:

    def getSubject(self,subjectId):
        try:
            subjectRepo = SubjectRepository()
            whereClause = ""
            params = ()
            if subjectId:
                whereClause = " AND s.subject_id=%s"
                params=(subjectId,)
            result = subjectRepo.findSubject(whereClause,params)
            return result
        except Exception as e:
            logger.error("SubjectService getSubject() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createSubject(self,subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable):
        try:
            subjectRepo = SubjectRepository()
            result = subjectRepo.createSubject(subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable)
            return result
        except Exception as e:
            logger.error("SubjectService createSubject() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def editSubject(self,subject_id, subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable):
        try:
            subjectRepo = SubjectRepository()
            result = subjectRepo.editSubject(subject_id, subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable)
            return result
        except Exception as e:
            logger.error("SubjectService editSubject() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteSubject(self,subjectId):
        try:
            subjectRepo = SubjectRepository()
            result = subjectRepo.deleteSubject(subjectId)
            return result
        except Exception as e:
            logger.error("SubjectService deleteSubject() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)