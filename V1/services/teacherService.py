import json

from V1.queries import userQuery
from V1.repositories.teacherRepository import TeacherRepository
from V1.repositories.userRepository import UserRepository
from V1.utils.transformUtils import TransformUtils
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("TeacherService")


class TeacherService:

    def getTeachers(self,teacherId):
        try:
            teacherRepo = TeacherRepository()
            whereClause = ""
            params = ()
            if teacherId:
                whereClause = " AND t.teacher_id=%s"
                params=(teacherId,)
            result = teacherRepo.findTeachers(whereClause,params)
            resultList = []
            for item in result:
                teacherModel = TransformUtils().toTeacherModel(item['user_id'], item['teacher_id'],
                                                               item['teacher_phone'], item['user_username'],
                                                               item['user_password'], item['prename_id'],
                                                               item['prename_text'], item['user_firstname'],
                                                               item['user_lastname'], item['user_email'],
                                                               item['user_type'])
                resultList.append(teacherModel)
            return resultList
        except Exception as e:
            logger.error("TeacherService getTeachers() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
