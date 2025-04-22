from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from app.utils.jwt_ import encode_token
from blog.settings import MANAGER

class UserManager(models.Manager):
    def login(self, account, password):
        if account == MANAGER.get('ACCOUNT') and password == MANAGER.get('PASSWORD'):
            return 200, "token"
        return 400, "error"
