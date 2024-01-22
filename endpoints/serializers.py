from rest_framework import serializers
from sensors.models import Sensor, SensorReading
from predictions.models import FloodPrediction
from alerts.models import FloodAlert

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SensorReadingSerializer(serializers.ModelSerializer):
    sensor = SensorSerializer()

    class Meta:
        model = SensorReading
        fields = '__all__'

class FloodPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodPrediction
        fields = '__all__'

class FloodAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodAlert
        fields = '__all__'
