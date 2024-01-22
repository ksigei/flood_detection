from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SensorReading(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    water_level = models.FloatField()  

    def __str__(self):
        return f"{self.sensor.name} - {self.timestamp} - Water Level: {self.water_level} meters"
