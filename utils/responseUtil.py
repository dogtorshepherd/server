from models.ResponseBasic import ResponseSuccessWithData


class ResponseUtil:
    def transformResponseSuccessWithData(self,data):
        return ResponseSuccessWithData(data)