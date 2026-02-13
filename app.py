import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import requests
import plotly.graph_objects as go

from backend_predictor import (
    predict_parking_occupancy,
    convert_to_24h
)

# ============================================================
# PAGE CONFIG (UNCHANGED)
# ============================================================
st.set_page_config(
    page_title="ParkMatrix AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# STYLES (UNCHANGED)
# ============================================================
st.markdown("""
<style>
html, body {
    font-family: 'Inter', sans-serif;
}
.main {
    padding-top: 1.2rem;
}
.header {
    text-align: center;
    padding-bottom: 1.5rem;
}
.logo {
    font-size: 2.6rem;
    font-weight: 800;
}
.subtitle {
    font-size: 1.1rem;
    color: #6b7280;
}
.card {
    background: #ffffff;
    border-radius: 18px;
    padding: 1.5rem;
    box-shadow: 0 8px 28px rgba(0,0,0,0.06);
}
.section-title {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 1rem;
}
.conclusion {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
    border-radius: 18px;
    padding: 1.6rem;
    border-left: 6px solid #6366f1;
}
.good { color: #059669; font-weight: 700; }
.medium { color: #d97706; font-weight: 700; }
.bad { color: #dc2626; font-weight: 700; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER (UNCHANGED)
# ============================================================
st.markdown("""
<div class="header">
    <div class="logo">🚗 ParkMatrix AI</div>
    <div class="subtitle">Smart Parking Availability Intelligence</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# HELPERS
# ============================================================

def geocode_location(place):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": place, "format": "json", "limit": 1}
    headers = {"User-Agent": "ParkMatrixAI"}
    r = requests.get(url, params=params, headers=headers, timeout=10)
    if r.status_code == 200 and r.json():
        return float(r.json()[0]["lat"]), float(r.json()[0]["lon"])
    return None, None


def evaluate_status(occ):
    if occ < 40:
        return "Easily Available", "good"
    elif occ < 70:
        return "Moderate Availability", "medium"
    else:
        return "Highly Congested", "bad"


# ============================================================
# LAYOUT (UNCHANGED)
# ============================================================
left, right = st.columns([1.05, 0.95], gap="large")

# ============================================================
# INPUT PANEL (UNCHANGED)
# ============================================================
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📍 Parking Details</div>', unsafe_allow_html=True)

    location = st.text_input("Location", placeholder="e.g. Nampally, Miyapur, Hitech City")

    zone_map = {
        "Z1 – Office Districts": "Z1",
        "Z2 – Hospitals": "Z2",
        "Z3 – Residential Areas": "Z3",
        "Z4 – Commercial Hubs": "Z4",
        "Z5 – Transit / Mixed Use": "Z5"
    }

    zone_label = st.selectbox("Parking Zone Type", list(zone_map.keys()))
    zone_id = zone_map[zone_label]

    date = st.date_input("Date", value=dt.date.today())

    st.markdown("### ⏰ Arrival Time (Exact)")
    c1, c2, c3 = st.columns(3)
    with c1:
        hour = st.number_input("Hour", 1, 12, 8)
    with c2:
        minute = st.number_input("Minute", 0, 59, 30)
    with c3:
        meridian = st.selectbox("AM / PM", ["AM", "PM"])

    analyze = st.button("🔍 Analyze Parking")
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# MAP (UNCHANGED)
# ============================================================
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🗺️ Area Map</div>', unsafe_allow_html=True)

    if location:
        lat, lon = geocode_location(location)
        if lat:
            st.map(pd.DataFrame({"lat":[lat], "lon":[lon]}), zoom=12)
        else:
            st.info("Location not found.")
    else:
        st.info("Enter a location to view map.")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# ANALYSIS (REAL CNN + LSTM ONLY)
# ============================================================
if analyze and location:
    hour_24 = convert_to_24h(hour, meridian)
    day = date.day

    occ = predict_parking_occupancy(zone_id, day, hour_24)

    if occ is None:
        st.error("Not enough historical data available for this zone and time.")
        st.stop()

    pattern = []
    for h in range(24):
        val = predict_parking_occupancy(zone_id, day, h)
        pattern.append(val if val is not None else np.nan)

    pattern = np.array(pattern)

    status, status_class = evaluate_status(occ)
    best_hour = int(np.nanargmin(pattern))

    st.markdown("## 📊 Parking Demand Across the Day")

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=list(range(24)),
        y=pattern,
        mode="lines+markers",
        line=dict(width=3),
        name="Predicted Occupancy"
    ))

    fig.add_vline(
        x=hour_24,
        line_dash="dash",
        annotation_text="Your Time",
        annotation_position="top"
    )

    fig.update_layout(
        height=420,
        xaxis_title="Hour of Day",
        yaxis_title="Occupancy (%)",
        template="plotly_white",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="conclusion">', unsafe_allow_html=True)
    st.markdown(f"""
### 🚦 Parking Status: <span class="{status_class}">{status}</span>

**Expected Occupancy at {hour}:{minute:02d} {meridian}:**  
### **{occ:.2f}%**
""", unsafe_allow_html=True)

    if occ < 40:
        st.markdown("✅ Parking should be quick and stress-free.")
    elif occ < 70:
        st.markdown("⚠️ Parking may take a few minutes.")
    else:
        st.markdown("❌ Expect difficulty — high congestion likely.")

    st.markdown(f"""
### 🟢 Best Alternative Time
**{best_hour}:00 hrs** — lowest predicted demand today
""")

    st.markdown('</div>', unsafe_allow_html=True)
