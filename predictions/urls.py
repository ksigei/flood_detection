from django.urls import path
from .views import get_flood_prediction

urlpatterns = [
    path('get_flood_prediction/', get_flood_prediction, name='get_flood_prediction'),
]
