from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('auth', views.AuthViewSet, basename='auth')
urlpatterns = [

] + router.urls