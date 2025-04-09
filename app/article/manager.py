from django.db import models
from .constant import ARTICLE_STATUS_PUBLISHED

class ArticleManager(models.Manager):
    def get_articles_list(self, page, size):
        return self.filter(status = ARTICLE_STATUS_PUBLISHED)[(page-1)*size : page*size]

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

