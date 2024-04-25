from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

router = DefaultRouter()
router.register("", CustomUserViewSet, basename="user")

urlpatterns = router.urls