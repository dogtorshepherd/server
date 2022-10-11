import json

from V1.queries import userQuery
from V1.repositories.adminRepository import AdminRepository
from V1.repositories.studentRepository import StudentRepository
from V1.repositories.teacherRepository import TeacherRepository
from V1.repositories.userRepository import UserRepository
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("UserService")


class UserService:

    def getUsers(self, userId):
        try:
            userRepo = UserRepository()
            whereClause = ""
            params = ()
            if userId:
                whereClause = " AND u.user_id=%s"
                params=(userId,)
            result = userRepo.getUsers(whereClause,params)
            return result
        except Exception as e:
            logger.error("UserService getUsers() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def userLogin(self, username, password):
        try:
            userRepo = UserRepository()
            result = userRepo.userLogin(username, password)
            return result
        except Exception as e:
            logger.error("UserService userLogin() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createUser(self, type, username, password, prename, firstname, lastname,data):
        try:
            userRepo = UserRepository()
            if prename == "นาย":
                prename = 1
            elif prename == "นาง":
                prename = 2
            elif prename == "นางสาว":
                prename = 3
            elif prename == "อ.ดร":
                prename = 4
            elif prename == "ผศ.ดร":
                prename = 5
            elif prename == "ศ.ดร":
                prename = 6
            else:
                prename = 1
            userResult = userRepo.createUser(type,username,password,prename,firstname,lastname)
            if type == "ADMIN":
                adminRepo = AdminRepository()
                userResult['adminId'] = adminRepo.insertAdmin(userResult['userId'],data['adminId'])
            elif type == "TEACHER":
                teacherRepo = TeacherRepository()
                userResult['teacherId'] = teacherRepo.inserTeacher(userResult['userId'],data['teacherId'],data['teacherPhone'])
            else:
                studentRepo = StudentRepository()
                userResult['studentId'] = studentRepo.insertStudent(userResult['userId'], data['studentId'],data['majorId'])

            return userResult
        except Exception as e:
            logger.error("UserService userLogin() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def editUser(self, userId, type, prename, firstname, lastname,data):
        try:
            userRepo = UserRepository()
            userResult = userRepo.editUser(type,prename,firstname,lastname, userId)
            if type == "ADMIN":
                adminRepo = AdminRepository()
                userResult['adminId'] = adminRepo.editAdmin(userResult['userId'],data['adminId'])
            elif type == "TEACHER":
                teacherRepo = TeacherRepository()
                userResult['teacherId'] = teacherRepo.editTeacher(userResult['userId'],data['teacherId'],data['teacherPhone'])
            else:
                studentRepo = StudentRepository()
                userResult['studentId'] = studentRepo.editStudent(userResult['userId'], data['studentId'],data['majorId'])

            return userResult
        except Exception as e:
            logger.error("UserService editUser() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteUser(self, userId):
        try:
            userRepo = UserRepository()
            userResult = userRepo.deleteUser(userId)

            return userResult
        except Exception as e:
            logger.error("UserService deleteUser() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def test(self):
        try:
            userRepo = UserRepository()
            userResult = userRepo.testQuery()
            return userResult
        except Exception as e:
            logger.error("UserService userLogin() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
