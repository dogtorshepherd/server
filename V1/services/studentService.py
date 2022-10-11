import json

from V1.queries import userQuery
from V1.repositories.studentRepository import StudentRepository
from V1.repositories.teacherRepository import TeacherRepository
from V1.repositories.userRepository import UserRepository
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("StudentService")


class StudentService:

    def getStudentOnGroup(self, groupId):
        try:
            studentRepo = StudentRepository()
            result = studentRepo.findStudentOnGroup(groupId)
            return result
        except Exception as e:
            logger.error("StudentService getTeachers() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def getStudentAll(self, userId, studentId, search):
        try:
            studentRepo = StudentRepository()
            whereCluse = ""
            params = ()
            if userId != "":
                whereCluse += " AND u.user_id=%s"
                params += (userId,)
            if studentId != "":
                whereCluse += " AND s.student_id=%s"
                params += (studentId,)

            if search != "":
                whereCluse += " AND (s.student_id LIKE %s OR u.user_firstname LIKE %s OR u.user_lastname LIKE %s)"
                txt = "%{text}%".format(text=search)
                params += (txt, txt, txt)

            if whereCluse != "":
                result = studentRepo.findStudent(whereCluse, params)
            else:
                result = studentRepo.findAllStudent()
            return result
        except Exception as e:
            logger.error("StudentService getStudentAll() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
