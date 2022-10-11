import json

from V1.queries import userQuery, teacherQuery, studentQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("StudentRepository")


class StudentRepository:
    dbConnector = DBConnector()

    def findStudentOnGroup(self,groupId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            params = (groupId,)
            self.cursor.execute(studentQuery.FIND_ALL_USERS_BY_GROUP_ID,params)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("StudentRepository findStudentOnGroup() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def insertStudent(self,userId,studentId,majorId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            params = (userId,studentId,majorId,)
            self.cursor.execute(studentQuery.INSERT_STUDENT,params)
            return True
        except Exception as e:
            logger.error("StudentRepository insertStudent() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def editStudent(self, userId, studentId, majorId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            params = (studentId, majorId, userId,)
            self.cursor.execute(studentQuery.EDIT_STUDENT, params)
            return True
        except Exception as e:
            logger.error("StudentRepository editStudent() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def findAllStudent(self):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(studentQuery.FIND_ALL_STUDENTS)
            return  self.cursor.fetchall()
        except Exception as e:
            logger.error("StudentRepository findAllStudent() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def findStudent(self,whereClause,params):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            logger.info("QUERY : " + studentQuery.FIND_STUDENT(whereClause))
            self.cursor.execute(studentQuery.FIND_STUDENT(whereClause),params)

            return  self.cursor.fetchall()
        except Exception as e:
            logger.error("StudentRepository findAllStudent() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()
