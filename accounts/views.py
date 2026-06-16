from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from django.shortcuts import render, redirect
from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer, UserCreateSerializer


# Create your views here.
class AuthViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_permissions(self):
        if self.action in ('logout_user', 'get_session'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]
    @action(methods=['post'], detail=False, url_path='login', serializer_class=LoginSerializer)
    def login_user(self, request):
        serialize = LoginSerializer(data=request.data)
        if serialize.is_valid():
            usser = serialize.validated_data['user']
            login(request, usser)
            return Response(UserSerializer(usser).data , status=status.HTTP_200_OK)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=False, url_path='logout')
    def logout_user(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(methods=['get'], detail=False, url_path='session', serializer_class=UserSerializer)
    def get_session(self, request):
        user = request.user
        return Response(UserSerializer(user).data , status=status.HTTP_200_OK)
