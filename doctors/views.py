from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Doctors
from rest_framework.mixins import CreateModelMixin


# Create your views here.
class DoctorsViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = Doctors.objects.all()
    serializer_class =