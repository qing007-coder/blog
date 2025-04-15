from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from app.article.models import Article
from app.article.serializer import ArticleSerializer


class ArticleView(viewsets.ViewSet):
    def handle_response(self, serializer, isUnserializable=False):
        if not isUnserializable:
            return Response(serializer.data, status=status.HTTP_200_OK)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['get'])
    def get_article_by_id(self, request, pk=None):
        try:
            article = Article.objects.get_article_by_id(id=pk)
            if article is None:
                return Response({"detail": "Article not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ArticleSerializer(article)
            return self.handle_response(serializer)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_list(self, request):
        try:
            page = int(request.query_params.get('page', 1))
            size = int(request.query_params.get('size', 10))
            category = request.query_params.get('category', None)
            articles = Article.objects.get_articles_list(page=page, size=size, category=category)
            # print(articles)
            serializer = ArticleSerializer(instance=articles, many=True)
            return self.handle_response(serializer)
        except ValueError:
            return Response({"error": "Invalid page or size parameter."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def publish_article(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            try:
                title = serializer.validated_data.get('title')
                content = serializer.validated_data.get('content')
                category = serializer.validated_data.get('category')
                article = Article.objects.create_article(title, content, category)
                serializer = ArticleSerializer(article)
                return self.handle_response(serializer)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def update_article(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            try:
                id = request.data.get('id')
                title = serializer.validated_data.get('title')
                content = serializer.validated_data.get('content')
                category = serializer.validated_data.get('category')
                article = Article.objects.update_article(id, title=title, content=content, category=category)
                serializer = ArticleSerializer(article)
                return self.handle_response(serializer)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def delete_article(self, request):
        id = request.data.get('id')

        isDeleted = Article.objects.delete_article(id)
        if isDeleted:
            return Response({"detail": "Article deleted."}, status=status.HTTP_200_OK)

        return Response({"detail": "Article not found."}, status=status.HTTP_404_NOT_FOUND)
