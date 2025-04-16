from rest_framework.routers import DefaultRouter
from .views import ArticleView, CategoryView

router = DefaultRouter()
# 注册视图集（虽然APIView不是ViewSet，但可以这样包装）
router.register(r'articles', ArticleView, basename='article')
router.register(r'categories', CategoryView, basename='category')

urlpatterns = router.urls