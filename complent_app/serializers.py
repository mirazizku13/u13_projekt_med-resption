from accounts.models import User
from rest_framework import serializers

from complent_app.models import Complent


class ComplentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complent
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
