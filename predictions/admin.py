from django.contrib import admin

# Register your models here.
from .models import FloodPrediction, HistoricalData

admin.site.register(FloodPrediction)
admin.site.register(HistoricalData)
