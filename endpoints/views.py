from rest_framework import generics
from sensors.models import Sensor, SensorReading
from predictions.models import FloodPrediction
from alerts.models import FloodAlert
from .serializers import SensorSerializer, SensorReadingSerializer, FloodPredictionSerializer, FloodAlertSerializer

class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorReadingListCreateView(generics.ListCreateAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer

class FloodPredictionListCreateView(generics.ListCreateAPIView):
    queryset = FloodPrediction.objects.all()
    serializer_class = FloodPredictionSerializer

class FloodAlertListCreateView(generics.ListCreateAPIView):
    queryset = FloodAlert.objects.all()
    serializer_class = FloodAlertSerializer
