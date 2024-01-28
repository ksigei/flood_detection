from django.urls import path
from .views import SensorReadingView, simulate_sensor

urlpatterns = [
    path('sensor-reading/', SensorReadingView.as_view(), name='sensor_reading'),
    path('simulate_sensor/', simulate_sensor, name='simulate_sensor'),
]
