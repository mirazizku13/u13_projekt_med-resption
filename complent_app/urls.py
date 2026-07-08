from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('complent', views.ComplentView, basename='complent')

urlpatterns = router.urls