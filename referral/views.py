from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from referral.models import Referral
from referral.serializers import ReferralSerializer


class ReferralViewSet(ModelViewSet):
    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer



