from django.urls import path
from .views import SpendStatisticView

urlpatterns = [
    path('spend', SpendStatisticView.as_view()),  # Создайте представление в соответствующем файле views.py
    # Добавьте другие маршруты, если нужно
]
