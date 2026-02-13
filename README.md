# 🚗 ParkMatrix AI

**Smart Parking Availability Intelligence using Deep Learning**

ParkMatrix AI predicts parking availability using a CNN-LSTM deep learning model trained on historical urban parking data.

---

## 🚀 Features
- Real-time parking availability prediction
- CNN + LSTM time-series forecasting
- Zone-based urban modeling
- Interactive Plotly visualizations
- Map-based location intelligence
- Exact arrival time analysis (12-hour format)

---

## 🧠 Model Architecture
- Conv1D → LSTM → Dense
- Input: Last 3 hours occupancy
- Output: Next-hour parking demand
- Trained on real parking datasets

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

---

# 🌐 STEP 5 — Push to GitHub

### Create repo
- Name: `parkmatrix-ai`
- Public

### Push code
```bash
git init
git add .
git commit -m "Initial commit: ParkMatrix AI"
git branch -M main
git remote add origin https://github.com/<your-username>/parkmatrix-ai.git
git push -u origin main


author - Puneeth raj yadav 