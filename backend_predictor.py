# backend_predictor.py

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model


# ---------------------------------------------------
# Load dataset and model ONCE
# ---------------------------------------------------

DATASET_PATH = "parking_dataset_sorted.csv"
MODEL_PATH = "cnn_lstm_parking_model.keras"

df = pd.read_csv(DATASET_PATH)
model = load_model(MODEL_PATH)


# ---------------------------------------------------
# Helper: convert 12-hour time to 24-hour
# ---------------------------------------------------

def convert_to_24h(hour, am_pm):
    hour = int(hour)

    if am_pm == "PM" and hour != 12:
        return hour + 12
    if am_pm == "AM" and hour == 12:
        return 0
    return hour


# ---------------------------------------------------
# CORE FUNCTION (THIS IS THE HEART OF THE PROJECT)
# ---------------------------------------------------

def predict_parking_occupancy(zone_id, day, hour_24):
    """
    Uses historical data + CNN-LSTM to predict next-hour occupancy
    """

    # We need last 3 hours
    past_hours = [hour_24 - 3, hour_24 - 2, hour_24 - 1]

    # Edge case (early hours)
    if min(past_hours) < 0:
        return None

    # Filter dataset
    history = df[
        (df["zone_id"] == zone_id) &
        (df["day"] == day) &
        (df["hour"].isin(past_hours))
    ].sort_values("hour")

    # If we don't have exactly 3 records → can't predict
    if len(history) != 3:
        return None

    # Extract occupancies
    occupancies = history["occupancy"].values

    # Normalize
    X = occupancies / 100.0

    # Reshape for CNN + LSTM → (1, 3, 1)
    X = X.reshape(1, 3, 1)

    # Predict
    prediction = model.predict(X, verbose=0)[0][0]

    # Denormalize
    predicted_occupancy = round(prediction * 100, 2)

    return predicted_occupancy
