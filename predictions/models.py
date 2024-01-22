from django.db import models

class FloodPrediction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    prediction_text = models.TextField()
    probability = models.FloatField(null=True, blank=True)  # Probability of the flood event

    def __str__(self):
        return f"{self.timestamp} - Prediction: {self.prediction_text} - Probability: {self.probability}"

class HistoricalData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    total_population = models.FloatField()
    total_croplands_area = models.FloatField()
    directly_aff_popn = models.FloatField()
    total_flooded_area = models.FloatField()  # Target variable

    def __str__(self):
        return f"{self.timestamp} - Historical Data"