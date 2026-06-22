import streamlit as st
import numpy as np
import pickle

# 1. Page Configuration Setup
st.set_page_config(
    page_title="Gold AI Valuation Hub",
    page_icon="🪙",
    layout="centered"
)

# 2. Premium Commodity Theme (CSS Background & Global Elements Styling)
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.95)), 
                          url("https://images.unsplash.com/photo-1610374792793-f016b77ca51a?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #f8fafc;
    }
    .stNumberInput div div input {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #fbbf24 !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 8px;
        font-weight: bold;
    }
    label p {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #d97706 0%, #b45309 100%);
        color: white;
        border-radius: 10px;
        border: none;
        padding: 14px 20px;
        font-size: 18px;
        font-weight: bold;
        box-shadow: 0 6px 20px rgba(180, 83, 94, 0.3);
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 15px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%);
        box-shadow: 0 0 25px #f59e0b;
        color: #0f172a;
    }
    .valuation-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 30px;
        background-color: rgba(30, 41, 59, 0.8);
        border: 2px solid #fbbf24;
        color: #fbbf24;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🪙 Gold Market AI Valuation Engine")
st.markdown("### Automated Predictive Analyst using Random Forest Regression")
st.write("Provide the 4 required financial market tracking metrics below.")
st.markdown("---")

# 3. Load Saved Model Artifact
try:
    with open('gold_model.sav', 'rb') as f_model:
        model = pickle.load(f_model)
except FileNotFoundError:
    st.error("🚨 File Loss Error: 'gold_model.sav' could not be found. Please save your model inside your notebook first.")
    st.stop()

st.markdown("#### Market Metrics Profile (4 Features)")

# Organizing 4 features cleanly into 2 columns
col1, col2 = st.columns(2)

with col1:
    spx = st.number_input("SPX Index Value (e.g., 1447.16)", min_value=0.0, value=1447.16, format="%.2f")
    uso = st.number_input("USO (United States Oil Fund Value)", min_value=0.0, value=78.47, format="%.2f")

with col2:
    slv = st.number_input("SLV (Silver Trust Value)", min_value=0.0, value=15.18, format="%.2f")
    eur_usd = st.number_input("EUR/USD Exchange Rate", min_value=0.0, value=1.4717, format="%.4f")

# 4. Prediction Execution
if st.button("CALCULATE MARKET ESTIMATE"):
    # Group features in the exact array order used to train the Random Forest
    features = [spx, uso, slv, eur_usd]
    
    # Reshape features to a 2D array (1 row, 4 columns)
    input_array = np.asarray(features).reshape(1, -1)
    
    # Run prediction
    prediction = model.predict(input_array)
    estimated_price = prediction[0]
    
    # Display the result in the premium styled valuation box
    st.markdown(
        f'<div class="valuation-box">'
        f'📈 ESTIMATED GOLD VALUE (GLD):<br>'
        f'<span style="font-size: 36px; color: #ffffff;">${estimated_price:,.2f}</span>'
        f'</div>', 
        unsafe_allow_html=True
    )
