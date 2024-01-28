from django.views.generic import View
from django.http import JsonResponse
from django.http import JsonResponse
import random
import time
from datetime import datetime
from predictions.ml import make_real_time_prediction
from .models import Sensor, SensorReading

class SensorReadingView(View):
    def post(self, request, *args, **kwargs):
        # Assuming you send sensor data in the request
        sensor_data = request.POST  # Adjust as per your data format

        # Make a real-time prediction using the trained ML model
        ml_model = load_trained_ml_model() 
        make_real_time_prediction(ml_model, sensor_data)

        return JsonResponse({"status": "success"})

def simulate_sensor(request):
    sensors = Sensor.objects.all()
    sensor = sensors.get(ip_address='127.0.0.1')  # Adjust the IP address as needed
    sensor_id = request.GET.get('sensor_id', sensor.id)
    parameters = request.GET.getlist('parameters', ['water_level', 'temperature', 'humidity'])
    num_readings = int(request.GET.get('num_readings', 2))
    interval_seconds = float(request.GET.get('interval_seconds', 1))

    def generate_sensor_reading():
        timestamp = datetime.utcnow()
        reading = {param: random.uniform(0, 100) for param in parameters}
        return SensorReading(sensor_id=sensor_id, timestamp=timestamp, water_level=reading['water_level'])

    def simulate_sensor():
        for _ in range(num_readings):
            reading = generate_sensor_reading()
            reading.save()  # Save the sensor reading to the database
            time.sleep(interval_seconds)

    simulate_sensor()
    return JsonResponse({"status": "success"})

            
