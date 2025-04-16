from rest_framework.response import Response
from rest_framework import status

def response(code, data, message=None):
    default_message = ''
    if not message:
        print('no message')
        match code:
            case status.HTTP_200_OK:
                message = 'success'
            case status.HTTP_400_BAD_REQUEST:
                message = 'bad request'
            case status.HTTP_404_NOT_FOUND:
                message = 'not found'
            case status.HTTP_405_METHOD_NOT_ALLOWED:
                message = 'method not allowed'
            case status.HTTP_500_INTERNAL_SERVER_ERROR:
                message = 'internal server error'

    return Response({
        'code': code,
        'data': data,
        'message': message,
    }, status=status.HTTP_200_OK)