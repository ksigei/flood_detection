from django.contrib import admin

# Register your models here.
from .models import Sensor, SensorReading

admin.site.register(Sensor)
admin.site.register(SensorReading)
