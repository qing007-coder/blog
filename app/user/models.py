from django.db import models
from app.base import model
from .manager import UserManager


class User(model.BaseModel):
    account = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    objects = UserManager()

    class Meta:
        db_table = 'user'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

