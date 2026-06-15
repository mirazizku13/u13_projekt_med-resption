from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response

from accounts.serializers import LoginSerializer, UserSerializer


# Create your views here.
class AuthViewSet(viewsets.ViewSet):
    @action(methods=['post'], detail=False, url_path='login')
    def login_user(self, request):
        serialize = LoginSerializer(request.data)
        if serialize.is_valid():
            username = serialize.data['username']
            password = serialize.data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)