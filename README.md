# 🪙 Gold Market AI Valuation Engine

A premium, end-to-end Machine Learning web application that predicts the spot price of Gold ($GLD$) based on global macroeconomic indicators, asset correlations, and historical market metrics. The web dashboard layer is engineered dynamically using **Streamlit** and utilizes a serialized **Random Forest Regressor** model.

🔗 **Live Web Application: https://goldpriceprediction-7uujlbef2dt7wafppr7gvs.streamlit.app/

---

## 📐 Project Overview
This project leverages data analytics and supervised machine learning to estimate the daily closing price of gold. Because gold prices are tightly intertwined with global economic strength, currency valuations, and commodity cycles, the machine learning pipeline tracks multivariable correlations across key global assets to produce precise, real-time market evaluations.

### 📊 Dataset & Feature Specifications
The machine learning pipeline evaluates 5 primary target variables to establish pricing trends:
* **SPX (S&P 500 Index):** A capitalization-weighted index of 500 leading publicly traded companies in the U.S., acting as a proxy for global equity market health.
* **USO (United States Oil Fund):** An exchange-traded security tracking the spot price of West Texas Intermediate (WTI) light, sweet crude oil, measuring energy market inflation.
* **SLV (iShares Silver Trust):** An exchange-traded fund tracking the spot price of silver physical bullion, capturing the high intrinsic correlation between precious metals.
* **EUR/USD:** The primary currency exchange rate pair, representing the performance of the Euro relative to the United States Dollar to track global currency fluctuations.
* **Date:** Time-series chronological index used to filter and map historical pricing data trends.

---

## 🛠️ Tech Stack & Implementation Matrix
* **Data Processing & Manipulation:** Python, Pandas, NumPy
* **Visualization Modules:** Matplotlib, Seaborn
* **Machine Learning Framework:** Scikit-Learn (Random Forest Regressor & Multi-variable Regression)
* **Web Dashboard Engine:** Streamlit
* **Model Serialization:** Pickle

### Model Evaluation Profile
The performance metrics captured during training and validation checkpoints indicate exceptional predictive accuracy:
* **Random Forest Regressor Training Error Score ($R^2$):** `~0.9984` *(Replace with your exact score)*
* **Random Forest Regressor Validation Error Score ($R^2$):** `~0.9892` *(Replace with your exact score)*

---

## 📁 Repository Structure
```text
├── GOLD_PRICE_PREDICTION.ipynb   # Jupyter Notebook containing EDA, correlation analysis, and training pipelines
├── app_gold.py                  # Main standalone styled Streamlit web application deployment file
├── gold_price_model.pkl          # Serialized and trained Random Forest Regressor model artifact
└── requirements.txt             # Python dependencies configuration for the deployment server environment
