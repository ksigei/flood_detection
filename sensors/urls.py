from django.urls import path
from .views import SensorReadingView

urlpatterns = [
    path('sensor-reading/', SensorReadingView.as_view(), name='sensor_reading'),
]
