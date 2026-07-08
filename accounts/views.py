from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from accounts.serializers import LoginSerializer, UserSerializer
# \

from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework import viewsets, status, permissions
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import LoginSerializer, UserSerializer, UserCreateSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class AuthViewSet(viewsets.GenericViewSet, CreateModelMixin , ListModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def get_permissions(self):
        if self.action in ('logout_user', 'get_session'):
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]

    @action(methods=['post'], detail=False, url_path='login', serializer_class=LoginSerializer)
    def login_user(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False, url_path='logout')
    def logout_user(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, url_path='session', serializer_class=UserSerializer)
    def get_session(self, request):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
