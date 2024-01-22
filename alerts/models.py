from django.db import models

class FloodAlert(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_message = models.TextField()
    recipients = models.TextField() 

    def __str__(self):
        return f"{self.timestamp} - Alert: {self.alert_message} (Sent to: {self.recipients})"
