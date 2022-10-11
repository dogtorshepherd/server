import json

from V1.queries import userQuery, teacherQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("TeacherRepository")


class TeacherRepository:
    dbConnector = DBConnector()

    def findTeachers(self,whereClause,params):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(teacherQuery.FIND_ALL_TEACHERS(whereClause),params)
            # logger.info("QUERY",teacherQuery.FIND_ALL_TEACHERS(whereClause))
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("TeacherRepository findTeachers() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def inserTeacher(self,userId,teacherId,teacherPhone):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(teacherQuery.INSERT_TEACHER,(userId,teacherId,teacherPhone))
            return True
        except Exception as e:
            logger.error("TeacherRepository findTeachers() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def editTeacher(self,userId,teacherId,teacherPhone):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(teacherQuery.EDIT_TEACHER,(teacherId,teacherPhone,userId))
            return True
        except Exception as e:
            logger.error("TeacherRepository findTeachers() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()
