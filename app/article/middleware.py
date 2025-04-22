import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app.utils.response import response
from functools import wraps
from app.utils.jwt_ import decode_token


class AuthMiddleware(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if not token:
            raise AuthenticationFailed('need token')
        try:
            data = decode_token(token)
            print(data)
            # print(data.get('account'))
            return data, token
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')


def custom_authenticate(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        auth = AuthMiddleware()
        try:
            user, token = auth.authenticate(request)
            request.user = user  # 没啥用 看看后面用不用扩展
            request.auth = token  # 没啥用
            return view_func(self, request, *args, **kwargs)
        except AuthenticationFailed as e:
            return response(400, None, message=e.detail)

    return wrapper
