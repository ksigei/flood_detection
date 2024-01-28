from django.urls import path
from .views import view_flood_alerts

urlpatterns = [
    path('view-flood-alerts/', view_flood_alerts, name='view_flood_alerts'),
]
