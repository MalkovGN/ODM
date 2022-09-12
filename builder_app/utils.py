from rest_framework.exceptions import APIException
from rest_framework import status


class LenRowException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'The length of the of is not 10'
    default_code = 'Invalid'


class NotFloatException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'The type is not float'
    default_code = 'Invalid'
