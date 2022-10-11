from flask import Blueprint, request, jsonify

from constants import http, httpError
from eventRouters.userEventRouter import UserEventRouter
from models.ErrorModel import ClientErrorModel, SystemErrorModel
from models.ResponseBasic import ResponseError
from modules.logger import Logger

logger = Logger().getLogger("UserRouter")
user_api = Blueprint('user', __name__)


@user_api.route("/users", methods=['GET'])
def users():
    try:
        version = request.headers.get("x-api-version")
        params = request.args.to_dict()
        if len(params) > 0:
            result = {
                '1.0.0': UserEventRouter().getAllUsers(params)
            }[version]
        else:
            result = {
                '1.0.0': UserEventRouter().getAllUsers({})
            }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("UserRouter users() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, str(e))
        return jsonify(ResponseError(error).__dict__), httpError.HTTP_UN_AUTHORIZATION_HTTP_CODE
    except Exception as e:
        logger.error("UserRouter users() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            error = SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE, httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,str(e))
            return jsonify(ResponseError(error).__dict__), error.httpCode
        error = SystemErrorModel(e.statusCode, e.message,e.stack)
        return jsonify(ResponseError(error) .__dict__), error.statusCode

@user_api.route("/user/login", methods=['POST'])
def login():
    try:
        version = request.headers.get("x-api-version")
        body = request.json

        result = {
            '1.0.0': UserEventRouter().userLogin(body)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("UserRouter login() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, e.__str__())
        return jsonify(error.__dict__), 401
    except Exception as e:
        logger.error("UserRouter login() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            return jsonify(SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                            httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,e.__str__())), httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE
        return jsonify(SystemErrorModel(e.statusCode, e.message,e.stack).__dict__), e.statusCode\

@user_api.route("/user", methods=['POST'])
def createUser():
    try:
        version = request.headers.get("x-api-version")
        body = request.json

        result = {
            '1.0.0': UserEventRouter().createUser(body)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("UserRouter createUser() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, e.__str__())
        return jsonify(error.__dict__), 401
    except Exception as e:
        logger.error("UserRouter createUser() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            return jsonify(SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                            httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,e.__str__())), httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE
        return jsonify(SystemErrorModel(e.statusCode, e.message,e.stack).__dict__), e.statusCode

@user_api.route("/user", methods=['PUT'])
def editUser():
    try:
        version = request.headers.get("x-api-version")
        body = request.json

        result = {
            '1.0.0': UserEventRouter().editUser(body)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("UserRouter editUser() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, e.__str__())
        return jsonify(error.__dict__), 401
    except Exception as e:
        logger.error("UserRouter editUser() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            return jsonify(SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                            httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,e.__str__())), httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE
        return jsonify(SystemErrorModel(e.statusCode, e.message,e.stack).__dict__), e.statusCode

@user_api.route("/user", methods=['DELETE'])
def deleteUser():
    try:
        version = request.headers.get("x-api-version")
        params = request.args.to_dict()

        result = {
            '1.0.0': UserEventRouter().deleteUser(params)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("UserRouter deleteUser() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, e.__str__())
        return jsonify(error.__dict__), 401
    except Exception as e:
        logger.error("UserRouter deleteUser() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            return jsonify(SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                            httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,e.__str__())), httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE
        return jsonify(SystemErrorModel(e.statusCode, e.message,e.stack).__dict__), e.statusCode

@user_api.route("/tests-result", methods=['POST'])
def test():
    try:
        version = request.headers.get("x-api-version")
        body = request.json

        result = {
            '1.0.0': UserEventRouter().test(body)
        }[version]
        return jsonify(result.__dict__), http.HTTP_SUCCESS_HTTP_CODE
    except KeyError as e:
        logger.error("UserRouter createUser() Exception : " + str(e))
        error = ClientErrorModel(httpError.HTTP_UN_AUTHORIZATION_STATUS_CODE, httpError.HTTP_NOT_VERSION_MSG, e.__str__())
        return jsonify(error.__dict__), 401
    except Exception as e:
        logger.error("UserRouter createUser() Exception : " + str(e))
        if not hasattr(e, 'statusCode'):
            return jsonify(SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                            httpError.HTTP_INTERNAL_SERVER_ERROR_MSG,e.__str__())), httpError.HTTP_INTERNAL_SERVER_ERROR_HTTP_CODE
        return jsonify(SystemErrorModel(e.statusCode, e.message,e.stack).__dict__), e.statusCode