from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import FloodAlert
from predictions.models import FloodPrediction, HistoricalData
from django.core.mail import send_mail

def send_flood_alert(alert_message, recipients):
    # Send email alerts to recipients
    subject = 'Flood Alert'
    message = alert_message
    from_email = 'your@example.com'  # Update with your email
    recipient_list = recipients.values_list('email', flat=True)  # Assuming recipients have email field
    send_mail(subject, message, from_email, recipient_list)

def check_flood_alert():
    # Load the latest flood prediction
    latest_prediction = FloodPrediction.objects.latest('timestamp')
    
    # Load the latest historical data
    latest_data = HistoricalData.objects.latest('timestamp')

    # Calculate the percentage of flooded area
    total_area = 100000 
    percentage_flooded = (latest_prediction.total_flooded_area / total_area) * 100

    # Define threshold for triggering alerts (e.g., 50% of the total area)
    alert_threshold = 50

    # Check if the percentage of flooded area exceeds the threshold
    if percentage_flooded >= alert_threshold:
        # Create a flood alert message
        alert_message = f"High probability of flooding detected ({percentage_flooded:.2f}% of the total area)."

        # Get recipients who should receive the alert
        recipients = User.objects.all()  # Example: All users in the system
        
        # Create a FloodAlert object and save it to the database
        flood_alert = FloodAlert.objects.create(alert_message=alert_message)
        flood_alert.recipients.set(recipients)

        # Send flood alert to recipients via email
        send_flood_alert(alert_message, recipients)

def flood_alert_scheduler():
    # Check for flood alerts every 5 minutes
    check_flood_alert()
    print(f"Flood alert checked at {timezone.now()}")

def view_flood_alerts(request):
    # Fetch the latest flood alerts from the database
    latest_alerts = FloodAlert.objects.order_by('-timestamp')[:10] 

    # Pass the latest alerts to the template for rendering
    context = {'latest_alerts': latest_alerts}
    return render(request, 'flood_alerts.html', context)


