from django.urls import path
from .views import SensorListCreateView, SensorReadingListCreateView, FloodPredictionListCreateView, FloodAlertListCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensor-readings/', SensorReadingListCreateView.as_view(), name='sensor-reading-list-create'),
    path('flood-predictions/', FloodPredictionListCreateView.as_view(), name='flood-prediction-list-create'),
    path('flood-alerts/', FloodAlertListCreateView.as_view(), name='flood-alert-list-create'),
]
