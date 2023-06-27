from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = 404


class IncorrectPasswordException(APIException):
    status_code = 400
