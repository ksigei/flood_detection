from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from .models import FloodAlert
from predictions.models import FloodPrediction, HistoricalData
from django.core.mail import send_mail

# def send_flood_alert(alert_message):
#     # recipients = User.objects.all()
#     email_array = ['sigeikiprono4@gmail.com']


#     # save the flood alert in the database
#     flood_alert = FloodAlert.objects.create(alert_message=alert_message)
#     # flood_alert.recipients.set(recipients)
#     flood_alert.save()

#     # Send email alerts to recipients
#     subject = 'Flood Alert'
#     message = alert_message
#     from_email = 'noreply@skillfam.com'
#     # recipient_list = recipients.values_list('email', flat=True)  
#     recipient_list = email_array
#     send_mail(subject, message, from_email, recipient_list)
def send_flood_alert(alert_message):
    email_array = ['sigeikiprono4@gmail.com']

    # save the flood alert in the database
    flood_alert = FloodAlert.objects.create(alert_message=alert_message)
    flood_alert.save()

    # Send email alerts to recipients
    subject = 'Flood Alert'
    message = alert_message
    from_email = 'noreply@skillfam.com'
    recipient_list = email_array
    send_mail(subject, message, from_email, recipient_list)

def flood_alerts(request):
    # call send_flood_alert
    alert_message = "Flood alert."
    send_flood_alert(alert_message)

    return render(request, 'flood_alerts.html')

def check_flood_alert():
    # load the latest flood prediction
    latest_prediction = FloodPrediction.objects.latest('timestamp')
    
    # load the latest historical data
    latest_data = HistoricalData.objects.latest('timestamp')

    # calculate the percentage of flooded area
    total_area = 100000 
    percentage_flooded = (latest_prediction.total_flooded_area / total_area) * 100

    # set threshold for triggering alerts (e.g., 50% of the total area)
    alert_threshold = 50

    # check if the percentage of flooded area exceeds the threshold
    if percentage_flooded >= alert_threshold:
        # create a flood alert message
        alert_message = f"High probability of flooding detected ({percentage_flooded:.2f}% of the total area)."

        # get recipients who should receive the alert
        # recipients = User.objects.all()  
        recipients = ['sigeikiprono4@gmail.com']
        
        # send flood alert to recipients and save it in the database
        # send_flood_alert(alert_message, recipients)
        send_flood_alert(alert_message)

def flood_alert_scheduler():
    # check for flood alerts every 5 minutes
    check_flood_alert()
    print(f"Flood alert checked at {timezone.now()}")

def view_flood_alerts(request):
    # latest flood alerts
    latest_alerts = FloodAlert.objects.order_by('-timestamp')[:10] 

    context = {'latest_alerts': latest_alerts}
    return render(request, 'flood_alerts.html', context)


