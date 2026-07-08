from django.shortcuts import render
from rest_framework import viewsets

from patients.models import Patient
from appointment.models import appointment


# Create your views here.
class PatientsView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
