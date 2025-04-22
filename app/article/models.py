from django.db import models

from app.article.manager import ArticleManager, CategoryManager
from app.base import model


class Category(models.Model):
    name = models.CharField(max_length=100)

    objects = CategoryManager()

    def __str__(self):
        return self.name


class Article(model.BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default=False)

    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # 按照这个排序 没有减号就是升序
