from django.urls import path, include
from rest_framework import routers

from patient import views
router = routers.DefaultRouter()
router.register('reg', views.PatientCreateViewSet, basename='reg')
urlpatterns = [
    path('<int:pk>/', views.PatientListAPIView.as_view()),
] + router.urls