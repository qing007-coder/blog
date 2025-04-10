from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from app.article.models import Article
from app.article.serializer import ArticleSerializer

# views.py
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

class ArticleView(ViewSet):  # 改为继承ViewSet
    @action(detail=True, methods=['get'])
    def get_article_by_id(self, request, pk=None):
        article = Article.objects.get_article_by_id(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def list(self, request):
        page = int(request.query_params.get('page', 1))
        size = int(request.query_params.get('size', 10))
        articles = Article.objects.get_articles_list(page=page, size=size)
        return Response(ArticleSerializer(articles, many=True).data)