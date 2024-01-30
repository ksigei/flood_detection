from django.urls import path
from .views import view_flood_alerts, send_flood_alert

urlpatterns = [
    path('view-flood-alerts/', view_flood_alerts, name='view_flood_alerts'),
    path('send_flood_alert', send_flood_alert, name='send_flood_alert')
]
