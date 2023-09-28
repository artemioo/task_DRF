from django.urls import path
from .views import SpendStatisticView

urlpatterns = [
    path('spend', SpendStatisticView.as_view()),
]
