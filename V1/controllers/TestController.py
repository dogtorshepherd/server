from constants import httpError, http
from models.ErrorModel import SystemErrorModel, ClientErrorModel
from models.ResponseBasic import ResponseBasic


class TestController:
    def test(self):
        try:
            return ResponseBasic(http.HTTP_SUCCESS_CODE,"TEST Api")
        except Exception as e:
            print(e)
            if not hasattr(e, 'httpCode'):
                raise SystemErrorModel(httpError.HTTP_INTERNAL_SERVER_ERROR_STATUS_CODE,
                                        httpError.HTTP_INTERNAL_SERVER_ERROR_MSG)
            raise SystemErrorModel(e.statusCode, e.message)