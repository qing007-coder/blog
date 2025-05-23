import jwt
import datetime
from dateutil import tz
from blog import settings


def encode_token(**kwargs):
    print(kwargs.items())
    payload = {
        'exp': datetime.datetime.now(tz=tz.UTC) + datetime.timedelta(seconds=settings.TOKEN_EXPIRATION_SECONDS),
    }

    for field, value in kwargs.items():
        payload[field] = value

    print(payload)
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token


def decode_token(token):
    try:
        # 尝试解密 token
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise
    except jwt.InvalidTokenError:
        raise
    except Exception as e:
        # 处理其他未知异常
        raise Exception(f"error: {str(e)}")