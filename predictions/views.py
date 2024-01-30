from django.shortcuts import render
from rest_framework.decorators import api_view
from .ml import load_trained_ml_model, make_real_time_prediction, get_latest_historical_data

@api_view(['GET'])
def get_flood_prediction(request):
    # Load the trained model
    model = load_trained_ml_model()

    # Load the latest historical data from the database
    latest_data = get_latest_historical_data()

    # Make a real-time prediction
    prediction = make_real_time_prediction(model, latest_data)

    # Extract the scalar value from the NumPy array
    prediction_scalar = prediction[0]

    # Calculate the percentage of flooded area
    total_area = 1000095
    percentage_flooded = (prediction_scalar / total_area) * 100

    # Prepare response data
    response_data = {
        'prediction': percentage_flooded,
        'message': 'Flood prediction retrieved successfully.'
    }

    # Render the template with prediction data
    return render(request, 'flood_prediction.html', {'prediction_data': response_data})
