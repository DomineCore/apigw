from rest_framework import status as http_status
from rest_framework.response import Response

class ResponseApi404(Response):
    def __init__(self,apiname):
        status = http_status.HTTP_404_NOT_FOUND
        data = {
            "result":False,
            "message":f"api {apiname} is not found"
        }
        super().__init__(data=data, status=status)
