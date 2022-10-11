import json

from V1.queries import quizGroupQuery, quizQuery
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.DBConnector import DBConnector
from modules.logger import Logger

logger = Logger().getLogger("CourseRepository")


class QuizRepository:
    dbConnector = DBConnector()

    def getQuiz(self,quizGroupId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(quizQuery.FIND_ALL_QUESTION,(quizGroupId,))

            return self.cursor.fetchall()
        except Exception as e:
            logger.error("QuizRepository getQuiz() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def createQuiz(self,quizQuestion, quizAnswer, quizPoint, quizStandard, quizGroupId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(quizQuery.INSERT_QUIZ,(quizQuestion, quizAnswer, quizPoint, quizStandard, quizGroupId,))

            return self.cursor.lastrowid
        except Exception as e:
            logger.error("QuizRepository createQuiz() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def updateQuiz(self,quizId,quizQuestion, quizAnswer, quizPoint, quizStandard, quizGroupId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(quizQuery.UPDATE_QUIZ,(quizQuestion, quizAnswer, quizPoint, quizStandard, quizGroupId,quizId))

            return True
        except Exception as e:
            logger.error("QuizRepository updateQuiz() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()

    def deleteQuiz(self,quizId):
        try:
            self.con = self.dbConnector.connect()
            self.cursor = self.dbConnector.getCursor()
            self.cursor.execute(quizQuery.DELETE_QUIZ,(quizId,))

            return True
        except Exception as e:
            logger.error("QuizRepository updateQuiz() Exception : " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
        finally:
            self.con.commit()
            self.cursor.close()
            self.con.close()
