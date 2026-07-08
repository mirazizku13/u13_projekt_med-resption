from django.shortcuts import render
from rest_framework import viewsets

from doctors.models import Doctor
from doctors.serializer import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer




