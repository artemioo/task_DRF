from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListAPIView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SpendStatistic

# =========== Serializers ============


class SpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpendStatistic
        fields = ('__all__')


# =============== Views =====================


class SpendStatisticView(ListAPIView):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendSerializer




