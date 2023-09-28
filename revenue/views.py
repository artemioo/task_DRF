from django.db.models import Sum, Count
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import RevenueStatistic


class RevenueSerializer(serializers.ModelSerializer):
    spend = serializers.SlugRelatedField(slug_field='name', read_only=True)
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    total_impressions = serializers.IntegerField(read_only=True)
    total_clicks = serializers.IntegerField(read_only=True)
    total_conversion = serializers.IntegerField(read_only=True)

    class Meta:
        model = RevenueStatistic
        fields = ('__all__')


class RevenueStatisticView(ListAPIView):
    serializer_class = RevenueSerializer
    ordering_fields = ['date', 'name']

    def get_queryset(self):
        objs = RevenueStatistic.objects.values('date', 'name') \
            .annotate(
            revenue=Sum('revenue'),
            total_spend=Sum('spend__spend'),
            total_impressions=Sum('spend__impressions'),
            total_clicks=Sum('spend__clicks'),
            total_conversion=Sum('spend__conversion')
        )

        return objs
