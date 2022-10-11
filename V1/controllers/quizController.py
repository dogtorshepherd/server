import json

from V1.services.quizService import QuizService
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger
from utils.responseUtil import ResponseUtil

logger = Logger().getLogger("QuizController")


class QuizController:
    def getQuiz(self):
        try:
            data = QuizService().getQuiz()
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("QuizController getQuiz Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def getQuizInfo(self, params):
        try:
            quizGroupId = ""
            if 'quiz_group_id' in params:
                quizGroupId = params['quiz_group_id']
            data = QuizService().getQuizInfo(quizGroupId)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("QuizController getQuiz Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createQuiz(self, body):
        try:
            quizDatabaseId = ""
            quizNum = ""
            quizObjective = ""
            quizType = ""
            quizStartDate = ""
            quizEndDate = ""
            quizStartTime = ""
            quizEndTime = ""
            quizSubjectGroupId = ""
            quizLists = []

            if 'quizDatabaseId' in body:
                quizDatabaseId = body['quizDatabaseId']

            if 'quizNum' in body:
                quizNum = body['quizNum']

            if 'quizObjective' in body:
                quizObjective = body['quizObjective']

            if 'quizType' in body:
                quizType = body['quizType']

            if 'quizStartDate' in body:
                quizStartDate = body['quizStartDate']

            if 'quizEndDate' in body:
                quizEndDate = body['quizEndDate']

            if 'quizStartTime' in body:
                quizStartTime = body['quizStartTime']

            if 'quizEndTime' in body:
                quizEndTime = body['quizEndTime']

            if 'quizLists' in body:
                quizLists = body['quizLists']

            if 'quizSubjectGroupId' in body:
                quizSubjectGroupId = body['quizSubjectGroupId']

            data = QuizService().createQuiz(quizDatabaseId, quizNum, quizObjective, quizType, quizStartDate,
                                            quizEndDate, quizStartTime, quizEndTime, quizSubjectGroupId, quizLists)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("QuizController getQuiz Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def updateQuiz(self, body):
        try:
            quizGroupId = ""
            quizDatabaseId = ""
            quizNum = ""
            quizObjective = ""
            quizType = ""
            quizStartDate = ""
            quizEndDate = ""
            quizStartTime = ""
            quizEndTime = ""
            quizSubjectGroupId = ""
            quizLists = []

            if 'quizGroupId' in body:
                quizGroupId = body['quizGroupId']

            if 'quizDatabaseId' in body:
                quizDatabaseId = body['quizDatabaseId']

            if 'quizNum' in body:
                quizNum = body['quizNum']

            if 'quizObjective' in body:
                quizObjective = body['quizObjective']

            if 'quizType' in body:
                quizType = body['quizType']

            if 'quizStartDate' in body:
                quizStartDate = body['quizStartDate']

            if 'quizEndDate' in body:
                quizEndDate = body['quizEndDate']

            if 'quizStartTime' in body:
                quizStartTime = body['quizStartTime']

            if 'quizEndTime' in body:
                quizEndTime = body['quizEndTime']

            if 'quizLists' in body:
                quizLists = body['quizLists']

            if 'quizSubjectGroupId' in body:
                quizSubjectGroupId = body['quizSubjectGroupId']

            data = QuizService().updateQuiz(quizGroupId, quizDatabaseId, quizNum, quizObjective, quizType,
                                            quizStartDate, quizEndDate, quizStartTime, quizEndTime, quizSubjectGroupId,
                                            quizLists)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("QuizController getQuiz Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteQuiz(self, body):
        try:
            quizGroupId = ""
            isDeleteGroup = False
            quizLists = []

            if 'isDeleteGroup' in body:
                isDeleteGroup = body['isDeleteGroup']

            if 'quizGroupId' in body:
                quizGroupId = body['quizGroupId']

            if 'quizLists' in body:
                quizLists = body['quizLists']

            data = QuizService().deleteQuiz(quizGroupId, isDeleteGroup, quizLists)
            responseSuccess = ResponseUtil().transformResponseSuccessWithData(data)
            return responseSuccess
        except Exception as e:
            logger.error("QuizController getQuiz Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, 'statusCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG, str(e))
            raise SystemErrorModel(e.statusCode, e.message, e.stack)
