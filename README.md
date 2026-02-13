<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>ParkMatrix AI – Smart Parking Availability Intelligence</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <style>
    body {
      margin: 0;
      font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      background: #f8fafc;
      color: #0f172a;
      line-height: 1.6;
    }

    .container {
      max-width: 1100px;
      margin: auto;
      padding: 40px 20px;
    }

    header {
      text-align: center;
      margin-bottom: 60px;
    }

    header h1 {
      font-size: 3rem;
      margin-bottom: 10px;
    }

    header p {
      font-size: 1.2rem;
      color: #475569;
    }

    section {
      background: #ffffff;
      border-radius: 18px;
      padding: 32px;
      margin-bottom: 40px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    }

    h2 {
      font-size: 1.9rem;
      margin-bottom: 15px;
      border-left: 6px solid #6366f1;
      padding-left: 14px;
    }

    h3 {
      margin-top: 30px;
      font-size: 1.4rem;
    }

    ul {
      padding-left: 20px;
    }

    li {
      margin-bottom: 8px;
    }

    code, pre {
      background: #0f172a;
      color: #e5e7eb;
      padding: 14px;
      border-radius: 10px;
      display: block;
      overflow-x: auto;
      margin-top: 15px;
      font-size: 0.95rem;
    }

    .screenshots {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 24px;
      margin-top: 25px;
    }

    .screenshot {
      background: #f1f5f9;
      border-radius: 14px;
      padding: 12px;
      text-align: center;
    }

    .screenshot img {
      width: 100%;
      border-radius: 10px;
    }

    .screenshot p {
      margin-top: 10px;
      font-weight: 600;
    }

    .highlight {
      background: linear-gradient(135deg, #eef2ff, #f8fafc);
      border-left: 6px solid #6366f1;
      padding: 20px;
      border-radius: 14px;
      margin-top: 20px;
    }

    footer {
      text-align: center;
      margin-top: 50px;
      color: #64748b;
    }
  </style>
</head>

<body>

  <div class="container">

    <!-- HEADER -->
    <header>
      <h1>🚗 ParkMatrix AI</h1>
      <p>Smart Parking Availability Intelligence using Deep Learning</p>
    </header>

    <!-- ABOUT -->
    <section>
      <h2>📌 About the Project</h2>
      <p>
        <strong>ParkMatrix AI</strong> is an end-to-end deep learning system that predicts
        urban parking availability using historical time-series data and a
        <strong>CNN-LSTM neural network</strong>.
      </p>
      <p>
        The application provides real-time predictions, interactive demand curves,
        and actionable insights to help users decide <strong>when parking will be easiest</strong>.
      </p>
    </section>

    <!-- FEATURES -->
    <section>
      <h2>🚀 Key Features</h2>
      <ul>
        <li>Real-time parking availability prediction</li>
        <li>CNN + LSTM deep learning time-series forecasting</li>
        <li>Zone-based urban modeling (Z1 – Z5)</li>
        <li>Exact arrival-time analysis (12-hour format)</li>
        <li>Interactive Plotly demand graphs</li>
        <li>Map-based location intelligence (OpenStreetMap)</li>
        <li>Best alternative parking time recommendation</li>
      </ul>
    </section>

    <!-- MODEL -->
    <section>
      <h2>🧠 Model Architecture</h2>
      <pre>
Input: Last 3 Hours Parking Occupancy
        ↓
     Conv1D Layer
        ↓
      LSTM Layer
        ↓
     Dense Layer
        ↓
Output: Next-Hour Parking Occupancy (%)
      </pre>

      <ul>
        <li><strong>Input:</strong> Occupancy of previous 3 hours</li>
        <li><strong>Output:</strong> Predicted occupancy percentage</li>
        <li><strong>Framework:</strong> TensorFlow / Keras</li>
        <li><strong>Inference:</strong> Real-time from trained `.keras` model</li>
      </ul>
    </section>

    <!-- SCREENSHOTS -->
    <section>
      <h2>🖼️ Screenshots</h2>

      <div class="screenshots">

        <div class="screenshot">
          <img src="https://github.com/pun33th45/Park-Matrix.AI/blob/ce36fb737163a63ca7b5a4dca4bfbe5c7dd9fc25/screenshots/interface.png?raw=true" />
          <p>Application Interface</p>
        </div>

        <div class="screenshot">
          <img src="https://github.com/pun33th45/Park-Matrix.AI/blob/ce36fb737163a63ca7b5a4dca4bfbe5c7dd9fc25/screenshots/graphical%20interpretation.png?raw=true" />
          <p>Graphical Interpretation</p>
        </div>

        <div class="screenshot">
          <img src="https://github.com/pun33th45/Park-Matrix.AI/blob/ce36fb737163a63ca7b5a4dca4bfbe5c7dd9fc25/screenshots/conclusion.png?raw=true" />
          <p>AI-Driven Conclusion</p>
        </div>

      </div>
    </section>

    <!-- REAL DL PROOF -->
    <section>
      <h2>🔬 Proof of Real Deep Learning</h2>

      <div class="highlight">
        <ul>
          <li>Predictions change when dataset values are modified</li>
          <li>Uses trained <code>cnn_lstm_parking_model.keras</code></li>
          <li>Requires exactly 3 historical hours to infer</li>
          <li>No rule-based or hardcoded logic</li>
          <li>Fails gracefully when data is insufficient</li>
        </ul>
      </div>
    </section>

    <!-- TECH STACK -->
    <section>
      <h2>📊 Tech Stack</h2>
      <ul>
        <li>Python</li>
        <li>Streamlit</li>
        <li>TensorFlow / Keras</li>
        <li>Plotly</li>
        <li>Pandas & NumPy</li>
        <li>OpenStreetMap (Nominatim API)</li>
      </ul>
    </section>

    <!-- RUN -->
    <section>
      <h2>▶️ Run Locally</h2>
      <pre>
pip install -r requirements.txt
streamlit run app.py
      </pre>
    </section>

    <!-- AUTHOR -->
    <section>
      <h2>👤 Author</h2>
      <p><strong>Puneeth Raj Yadav</strong></p>
      <p>Aspiring Software Engineer | Deep Learning & Full-Stack Projects</p>
    </section>

    <footer>
      <p>© 2026 ParkMatrix AI — Built with Deep Learning</p>
    </footer>

  </div>

</body>
</html>
