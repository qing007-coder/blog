from django.db import models
from pandas.core.ops import arithmetic_op

from .constant import *

class ArticleManager(models.Manager):
    def get_articles_list(self, page, size, category):
        queryset = self.filter(status=ARTICLE_STATUS_PUBLIC)
        # 如果 category 存在，则添加 category 的过滤条件
        if category:
            queryset = queryset.filter(category=category)
        # 进行分页操作
        return queryset[(page - 1) * size: page * size]

    def create_article(self, title, content, category):
        article = self.model(
            title=title,
            content=content,
            status=ARTICLE_STATUS_PUBLIC,
            category=category,
        )

        article.save()
        return article

    def get_article_by_id(self, id):
        try:
            return self.get(id=id)
        except self.model.DoesNotExist:
            return None

    def update_article(self, id, **kwargs):
        article = self.get_article_by_id(id)
        if article:
            for field, value in kwargs.items():
                setattr(article, field, value)
            article.save()
            return article
        return None

    def delete_article(self, id):
        article = self.get_article_by_id(id)
        if article:
            article.delete()
            return True
        return False

class CategoryManager(models.Manager):
    def create_category(self, name):
        category = self.model(name=name)
        category.save()

        return category

    def delete_category(self, id):
        try:
            category =  self.get(id=id)
            category.delete()
            return True
        except self.model.DoesNotExist:
            return False

    def get_list(self):
        categories = self.filter()

        return categories