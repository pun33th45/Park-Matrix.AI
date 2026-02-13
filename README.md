# 🚗 ParkMatrix AI

**Smart Parking Availability Intelligence using Deep Learning**

ParkMatrix AI predicts urban parking availability using a **CNN–LSTM deep learning model**
trained on real historical parking data.

---

## 🚀 Features

- Real-time parking availability prediction
- CNN + LSTM time-series forecasting
- Zone-based urban modeling (Z1 – Z5)
- Interactive Plotly visualizations
- Map-based location intelligence (OpenStreetMap)
- Exact arrival time analysis (12-hour format)
- Best alternative parking time suggestion

---

## 🧠 Model Architecture

Input: Last 3 Hours Parking Occupancy
↓
Conv1D Layer
↓
LSTM Layer
↓
Dense Layer
↓
Output: Next-Hour Parking Occupancy (%)

**Input:** Occupancy values of previous 3 hours  
- **Output:** Predicted parking demand (%)  
- **Framework:** TensorFlow / Keras  
- **Inference:** Real-time using trained `.keras` model  

---

## 🖼️ Screenshots

### 🔹 Application Interface
![Interface](https://github.com/pun33th45/Park-Matrix.AI/blob/ce36fb737163a63ca7b5a4dca4bfbe5c7dd9fc25/screenshots/interface.png)

---

### 🔹 Graphical Interpretation
![Graph](https://github.com/pun33th45/Park-Matrix.AI/blob/ce36fb737163a63ca7b5a4dca4bfbe5c7dd9fc25/screenshots/graphical%20interpretation.png)

---

### 🔹 AI Conclusion
![Conclusion](https://github.com/pun33th45/Park-Matrix.AI/blob/ce36fb737163a63ca7b5a4dca4bfbe5c7dd9fc25/screenshots/conclusion.png)

---

## 🔬 Proof This Is a Real Deep Learning Project

- Predictions change when dataset values are modified
- Uses trained `cnn_lstm_parking_model.keras`
- Requires **exactly 3 historical hours** for inference
- No hardcoded rules or fake logic
- Model fails gracefully if data is insufficient

---

## 📊 Tech Stack

- Python  
- Streamlit  
- TensorFlow / Keras  
- Plotly  
- Pandas / NumPy  
- OpenStreetMap (Nominatim API)

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
👤 Author
Puneeth Raj Yadav
Aspiring Software Engineer | Deep Learning & Full-Stack Projects

