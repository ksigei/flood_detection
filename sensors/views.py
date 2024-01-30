from django.views.generic import View
from django.http import JsonResponse
from django.http import JsonResponse
import random
import time
from datetime import datetime
from predictions.ml import make_real_time_prediction
from .models import Sensor, SensorReading
from alerts.views import send_flood_alert
from predictions.ml import load_trained_ml_model
class SensorReadingView(View):
    def post(self, request, *args, **kwargs):
        sensor_data = request.POST  

        #real-time prediction using the trained ML model
        ml_model = load_trained_ml_model() 
        make_real_time_prediction(ml_model, sensor_data)

        return JsonResponse({"status": "success"})

def simulate_sensor(request):
    sensors = Sensor.objects.all()
    sensor = sensors.get(ip_address='127.0.0.1')  # IP address
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
            reading.save()  # save the reading
            
            # Check if the water level exceeds a certain threshold
            if reading.water_level > 20:  # adjustable water level threshold
                alert_message = f"High water level detected: {reading.water_level}"
                send_flood_alert(alert_message)  # call send flood alert
                
            time.sleep(interval_seconds)

    simulate_sensor()
    return JsonResponse({"status": "success"})