from rest_framework import serializers

from patient.models import Patient

class PatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    telephone_number = serializers.IntegerField()
    email = serializers.EmailField()
    description = serializers.CharField()
    times = serializers.IntegerField()

class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'age', 'telephone_number', 'email', 'description', 'times')
        extra_kwargs = {'id': {'read_only': True}}

