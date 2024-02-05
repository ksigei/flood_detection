from django.urls import path
from .views import view_flood_alerts, flood_alerts

urlpatterns = [
    path('view-flood-alerts/', view_flood_alerts, name='view_flood_alerts'),
    path('send_flood_alert', flood_alerts, name='send_flood_alert')
]
