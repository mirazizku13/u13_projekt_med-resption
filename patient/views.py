from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from patient.models import Patient
from patient.serializers import PatientCreateSerializer, PatientListSerializer

class PatientListAPIView(APIView):
    def get(self, request, pk=None):
        patients = Patient.objects.filter(pk=pk)
        serializer = PatientListSerializer(patients, many=True)
        return Response(serializer.data)
#
# class PatientViewSet(ViewSet):
#     def list(self, request):
#         patients = Patient.objects.all()
#         serializer = PatientListSerializer(patients, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = PatientCreateSerializer
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#         pass

class PatientCreateViewSet(viewsets.GenericViewSet, CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer