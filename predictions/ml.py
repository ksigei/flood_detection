from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from .models import HistoricalData, FloodPrediction
import joblib
import geopandas as gpd
import pandas as pd
import os

MODEL_DIRECTORY = './predictions/model/'
MODEL_PATH = os.path.join(MODEL_DIRECTORY, 'trained_model.joblib')

def train_ml_model():
    # Load data
    file_path = './dataset/data.geojson.txt'
    gdf = gpd.read_file(file_path)

    # Assume 'total_flooded_area' is the target variable
    target_variable = 'total_flooded_area'

    # Drop rows with missing target values
    gdf = gdf.dropna(subset=[target_variable])

    # Select relevant features
    features = gdf[['total_population', 'total_croplands_area', 'directly_aff_popn']]

    # Check if there are still missing values in features (handle them as needed)
    features = features.dropna()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, gdf[target_variable], test_size=0.2, random_state=42)

    # Initialize and train the machine learning model (Random Forest Regressor)
    model = RandomForestRegressor()
    
    # Check if there are still missing values in X_train and y_train 
    X_train = X_train.dropna()
    y_train = y_train.dropna()

    model.fit(X_train, y_train)

    # Create the model directory if it doesn't exist
    os.makedirs(MODEL_DIRECTORY, exist_ok=True)

    # Save the trained model to a file in the specified directory
    joblib.dump(model, MODEL_PATH)

def load_trained_ml_model():
    # Check if the model file exists before loading
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

def make_real_time_prediction(model, new_data):
    # Convert the dictionary to a DataFrame
    new_data_df = pd.DataFrame([new_data])

    # Assuming new_data_df has the same structure as training features
    prediction = model.predict(new_data_df)
    return prediction

def make_prediction():
    # Load the trained model
    model = load_trained_ml_model()

    # Load the latest historical data
    latest_data = get_latest_historical_data()

    # Make a prediction
    prediction = make_real_time_prediction(model, latest_data)

    # Extract the scalar value from the NumPy array
    prediction_scalar = prediction[0]

    # Calculate the percentage of flooded area
    total_area = 100000 
    percentage_flooded = (prediction_scalar / total_area) * 100

    # Output the prediction as a percentage
    print(f"Prediction: {percentage_flooded:.2f}% of the total area")

def get_latest_historical_data():
    # Get the latest historical data
    latest_data = HistoricalData.objects.latest('timestamp')

    return {
        'total_population': latest_data.total_population,
        'total_croplands_area': latest_data.total_croplands_area,
        'directly_aff_popn': latest_data.directly_aff_popn
    }

if __name__ == '__main__':
    train_ml_model()
    make_prediction()
