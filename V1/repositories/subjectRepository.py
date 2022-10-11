import json

from V1.queries import userQuery, teacherQuery, subjectQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("SubjectRepository")


class SubjectRepository:
    dbConnector = DBConnector()

    def findSubject(self,whereClause,params):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(subjectQuery.FIND_ALL_SUBJECT(whereClause),params)
            return self.cursor.fetchall()
        except Exception as e:
            logger.error("SubjectRepository findSubject() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def createSubject(self,subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(subjectQuery.INSERT_SUBJECT,(subject_code, subject_name, subject_decription, subject_year, 1, enable))
            result = {}
            result["subject_id"] = self.cursor.lastrowid
            result["subject_name"] = subject_name
            return result

        except Exception as e:
            self.con.rollback()
            logger.error("UserRepository createSubject Exception: " + json.dumps(e.__dict__))
            self.con.rollback()
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def editSubject(self,subject_id, subject_code, subject_name, subject_decription, course_name, subject_year, course_id, group, enable):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(subjectQuery.EDIT_SUBJECT,(subject_code, subject_name, subject_decription, subject_year, course_id, enable, subject_id))
            result = {}
            result["subject_id"] = subject_id
            result["subject_name"] = subject_name
            return result

        except Exception as e:
            self.con.rollback()
            logger.error("UserRepository editSubject Exception: " + json.dumps(e.__dict__))
            self.con.rollback()
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def deleteSubject(self,subjectId):
        try:
            logger.info(subjectId)
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(subjectQuery.DELETE_SUBJECT,(subjectId,))
            result = {}
            result["subjectId"] = subjectId
            return result

        except Exception as e:
            self.con.rollback()
            logger.error("UserRepository deleteSubject Exception: " + json.dumps(e.__dict__))
            self.con.rollback()
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()