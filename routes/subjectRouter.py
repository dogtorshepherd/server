from flask import Blueprint, request, jsonify

from constants import http, httpError
from eventRouters.subjectEventRouter import SubjectEventRouter
from eventRouters.teacherEventRouter import TeacherEventRouter
from eventRouters.userEventRouter import UserEventRouter
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from models.ResponseBasic import ResponseError
from modules.logger import Logger

logger = Logger().getLogger("SubjectRouter")
subject_api = Blueprint('subject', __name__)


@subject_api.route("/subjects", methods=['GET'])
def subject():
    try:
        version = request.headers.get("x-api-version")
        params = request.args.to_dict()
        if len(params) > 0:
            result = {
                '1.0.0': SubjectEventRouter().getSubjects(params)
            }[version]
        else:
            result = {
                '1.0.0': SubjectEventRouter().getSubjects({})
            }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), httpError.HTTP_UN_AUTHORIZATION_HTTP_CODE
    except Exception as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode, e.message,e.stack)
        return jsonify(ResponseError(error) .__dict__), error.statusCode

@subject_api.route("/subject", methods=['POST'])
def createSubject():
    try:
        version = request.headers.get("x-api-version")
        body = request.json

        result = {
            '1.0.0': SubjectEventRouter().createSubjects(body)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), httpError.HTTP_UN_AUTHORIZATION_HTTP_CODE
    except Exception as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode, e.message,e.stack)
        return jsonify(ResponseError(error) .__dict__), error.statusCode

@subject_api.route("/subject", methods=['PUT'])
def editSubject():
    try:
        version = request.headers.get("x-api-version")
        body = request.json

        result = {
            '1.0.0': SubjectEventRouter().editSubject(body)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), httpError.HTTP_UN_AUTHORIZATION_HTTP_CODE
    except Exception as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode, e.message,e.stack)
        return jsonify(ResponseError(error) .__dict__), error.statusCode

@subject_api.route("/subject", methods=['DELETE'])
def deleteSubject():
    try:
        version = request.headers.get("x-api-version")
        params = request.args.to_dict()

        result = {
            '1.0.0': SubjectEventRouter().deleteSubject(params)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("SubjectRouter deleteSubject() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), httpError.HTTP_UN_AUTHORIZATION_HTTP_CODE
    except Exception as e:
        logger.error("SubjectRouter subject() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode, e.message,e.stack)
        return jsonify(ResponseError(error) .__dict__), error.statusCode