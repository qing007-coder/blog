from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from app.utils.jwt_ import encode_token

class UserManager(models.Manager):
    def login(self, account, password):
        try:
            user = self.filter(account=account)
            print(user.get(password))
            print(user.values(password))
            # if check_password(password, user.values('password')):
            #     return
            return 200, "token"
        except self.model.DoesNotExist:
            return '未找到此用户'