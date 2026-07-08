from django.shortcuts import render
from rest_framework import viewsets, filters

from complent_app.models import Complent
from complent_app.serializers import ComplentSerializer
from patients.models import Patient


# Create your views here.
class ComplentView(viewsets.ModelViewSet):
    queryset = Complent.objects.all()
    serializer_class = ComplentSerializer

    def get_queryset(self):
        return Complent.objects.filter(
            patient__user=self.request.user
        )

    def perform_create(self, serializer):
        patient = Patient.objects.get(user=self.request.user)
        serializer.save(patient=patient)