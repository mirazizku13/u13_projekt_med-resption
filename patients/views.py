from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Patient
from .serializer import PatientSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    