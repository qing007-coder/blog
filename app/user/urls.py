from rest_framework.routers import DefaultRouter
from .views import UserView

router = DefaultRouter()
# 注册视图集（虽然APIView不是ViewSet，但可以这样包装）
router.register(r'user', UserView, basename='user')

urlpatterns = router.urls