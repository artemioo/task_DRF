from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import SpendStatistic
from django.db.models import Sum, F
from revenue.models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = RevenueStatistic
        fields = ('__all__')


class SpendSerializer(serializers.ModelSerializer):
    revenue = serializers.SerializerMethodField()

    class Meta:
        model = SpendStatistic
        fields = ('__all__' )

    def get_revenue(self, obj):
        revenue = obj.children.all() if isinstance(obj, SpendStatistic) else []
        serializer = RevenueSerializer(revenue, many=True)
        return serializer.data


class SpendStatisticView(ListAPIView):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendSerializer

    def get_queryset(self):
        objs = SpendStatistic.objects.values('date', 'name') \
            .annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
        )
        return objs
