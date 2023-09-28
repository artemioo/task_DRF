from django.urls import path
from .views import RevenueStatisticView

urlpatterns = [
    path('revenue', RevenueStatisticView.as_view()),
]