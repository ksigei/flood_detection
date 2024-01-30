from django.shortcuts import render
from sensors.models import SensorReading
import matplotlib.pyplot as plt
import io
import base64
from predictions.models import HistoricalData

def plot_historical_data():
    # Fetch historical data from the database
    historical_data = HistoricalData.objects.all()

    # Extract data for plotting
    timestamps = [data.timestamp for data in historical_data]
    total_population = [data.total_population for data in historical_data]
    total_croplands_area = [data.total_croplands_area for data in historical_data]
    directly_aff_popn = [data.directly_aff_popn for data in historical_data]
    total_flooded_area = [data.total_flooded_area for data in historical_data]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, total_population, label='Total Population')
    plt.plot(timestamps, total_croplands_area, label='Total Croplands Area')
    plt.plot(timestamps, directly_aff_popn, label='Directly Affected Population')
    plt.plot(timestamps, total_flooded_area, label='Total Flooded Area')
    
    # Customize the plot
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Historical Data')
    plt.legend()
    plt.grid(True)

    # Save the plot as an image file
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode the image bytes as base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    return f"data:image/png;base64,{image_base64}"

def home(request):
    # Fetch sensor readings (assuming you have multiple sensors)
    readings = SensorReading.objects.all()

    # Prepare data for the graph
    timestamps = [reading.timestamp for reading in readings]
    water_levels = [reading.water_level for reading in readings]

    # Create a Matplotlib figure
    plt.plot(timestamps, water_levels)
    plt.xlabel('Timestamp')
    plt.ylabel('Water Level (meters)')
    plt.title('Sensor Reading Graph')

    # Save the Matplotlib figure as an image file
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode the image file as a base64 string

    sensor_reading_graph = f"data:image/png;base64,{base64.b64encode(buf.getvalue()).decode('utf-8')}"

    plot_path = plot_historical_data()

    # Context data for rendering
    context = {'graph_img': sensor_reading_graph, 'plot_path': plot_path}

    return render(request, 'home.html', context)