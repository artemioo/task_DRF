from django.db.models import Sum
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
    queryset = None
    serializer_class = SpendSerializer

    def get_queryset(self):
        objs = SpendStatistic.objects.values('name', 'date').annotate(
            spend=Sum('spend'),
            impressions=Sum('impressions'),
            clicks=Sum('clicks'),
            conversion=Sum('conversion'),

        )
        return objs

