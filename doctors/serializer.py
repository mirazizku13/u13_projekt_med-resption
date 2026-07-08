from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id","user","specialization","procedure_cost",]






