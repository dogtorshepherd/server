import json

from V1.repositories.quizGroupRepository import QuizGroupRepository
from V1.repositories.quizRepository import QuizRepository
from V1.utils.transformUtils import TransformUtils
from constants import httpError
from models.ErrorModel import SystemErrorModel
from modules.logger import Logger

logger = Logger().getLogger("QuizService")


class QuizService:

    def getQuiz(self):
        try:
            quizRepo = QuizRepository()
            quizGroupRepo = QuizGroupRepository()
            result = quizGroupRepo.getQuizGroup()

            for item in result:
                item['quiz'] = quizRepo.getQuiz(item['quiz_group_id'])

            return result
        except Exception as e:
            logger.error("QuizService getQuiz() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def getQuizInfo(self,quizGroupId):
        try:
            quizRepo = QuizRepository()
            quizGroupRepo = QuizGroupRepository()
            result = quizGroupRepo.getQuizGroupById(quizGroupId)

            result['quiz'] = quizRepo.getQuiz(result['quiz_group_id'])

            return result
        except Exception as e:
            logger.error("QuizService getQuiz() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def createQuiz(self,quizDatabaseId,quizNum,quizObjective,quizType,quizStartDate,quizEndDate,quizStartTime,quizEndTime,quizSubjectGroupId,quizLists):
        try:
            quizRepo = QuizRepository()
            quizGroupRepo = QuizGroupRepository()
            #`database_id`, `quiz_objective`, `quiz_num`, `quiz_type`, `quiz_start_date`, `quiz_end_date`, `quiz_start_time`, `quiz_end_time`, `subject_group_id`
            params=(quizDatabaseId,quizObjective,quizNum,quizType,quizStartDate,quizEndDate,quizStartTime,quizEndTime,quizSubjectGroupId)
            quizGroupId = quizGroupRepo.createQuizGroup(params)
            result = {'quizGroupId': quizGroupId , 'createSuccess': True}
            result['quiz'] = []



            for quiz in quizLists:
                #`quiz_question`, `quiz_answer`, `quiz_point`, `quiz_standard`, `quiz_group_id`
                quizId = quizRepo.createQuiz(quiz['quizQuestion'],quiz['quizAnswer'],quiz['quizPoint'],quiz['quizStandard'],quizGroupId)
                result['quiz'].append({'quizId': quizId, 'createSuccess': True})

            return result
        except Exception as e:
            logger.error("QuizService createQuiz() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def updateQuiz(self,quizGroupId,quizDatabaseId,quizNum,quizObjective,quizType,quizStartDate,quizEndDate,quizStartTime,quizEndTime,quizSubjectGroupId,quizLists):
        try:
            quizRepo = QuizRepository()
            quizGroupRepo = QuizGroupRepository()
            #`database_id`, `quiz_objective`, `quiz_num`, `quiz_type`, `quiz_start_date`, `quiz_end_date`, `quiz_start_time`, `quiz_end_time`, `subject_group_id`
            params=(quizDatabaseId,quizObjective,quizNum,quizType,quizStartDate,quizEndDate,quizStartTime,quizEndTime,quizSubjectGroupId,quizGroupId)
            quizGroupRepo.updateQuizGroup(params)
            result = {'quizGroupId': quizGroupId , 'updateSuccess': True}
            result['quiz'] = []



            for quiz in quizLists:
                #`quiz_question`, `quiz_answer`, `quiz_point`, `quiz_standard`, `quiz_group_id`
                quizRepo.updateQuiz(quiz['quizQuestion'],quiz['quizAnswer'],quiz['quizPoint'],quiz['quizStandard'],quizGroupId,quiz['quizId'])
                result['quiz'].append({'quizId': quiz['quizId'], 'updateSuccess': True})

            return result
        except Exception as e:
            logger.error("QuizService updateQuiz() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)

    def deleteQuiz(self,quizGroupId,isDeleteGroup,quizLists):
        try:
            quizRepo = QuizRepository()
            quizGroupRepo = QuizGroupRepository()
            #`database_id`, `quiz_objective`, `quiz_num`, `quiz_type`, `quiz_start_date`, `quiz_end_date`, `quiz_start_time`, `quiz_end_time`, `subject_group_id`
            result = {}
            if isDeleteGroup:
                quizGroupRepo.deleteQuizGroup(quizGroupId)
                result = {'quizGroupId': quizGroupId , 'deleteSuccess': True}
            else:
                result = {'quizGroupId': quizGroupId, 'quiz': [], 'updateSuccess': True}
                for quiz in quizLists:
                    quizRepo.deleteQuiz(quiz['quizId'])
                    result['quiz'].append({'quizId': quiz['quizId'], 'deleteSuccess': True})

            return result
        except Exception as e:
            logger.error("QuizService deleteQuiz() Exception: " + json.dumps(e.__dict__))
            if not hasattr(e, "statusCode"):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                       httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message, e.stack)