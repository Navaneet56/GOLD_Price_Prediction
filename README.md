# 🚗 Automotive Market AI Valuation Engine

A premium, end-to-end Machine Learning web application that predicts the resale price of used vehicles based on their detailed specification profiles and historical usage metrics. The web dashboard layer is engineered dynamically using **Streamlit** and utilizes a serialized **Linear Regression** model.

🔗 **Live Web Application: https://carpriceprediction-kfchvmd9dwkak72sjsrcr4.streamlit.app/

---

## 📐 Project Overview
This project leverages data analytics and supervised machine learning to estimate the current market value of used cars. The dataset tracks several structural and operational factors that dictate pricing trends in the secondary automotive market, enabling instant valuation predictions based on key entry metrics.

### 📊 Dataset & Feature Specifications
The machine learning pipeline evaluates 7 primary target variables:
* **Year of Manufacture:** The exact fiscal year the vehicle was produced.
* **Present_Price:** The original baseline ex-showroom price of the vehicle (expressed in Lakhs).
* **Kms_Driven:** Total absolute distance accumulated by the vehicle via its odometer record.
* **Fuel_Type:** Powertrain energy infrastructure (Categorically encoded: Petrol = 0, Diesel = 1, CNG = 2).
* **Seller_Type:** Upstream market distribution source (Categorically encoded: Dealer = 0, Individual = 1).
* **Transmission:** Transmission gearbox mechanics (Categorically encoded: Manual = 0, Automatic = 1).
* **Owner:** Number of previous independent registered owners.

---

## 🛠️ Tech Stack & Implementation Matrix
* **Data Processing & Manipulation:** Python, Pandas, NumPy
* **Visualization Modules:** Matplotlib, Seaborn
* **Machine Learning Framework:** Scikit-Learn (Linear Regression & Lasso Regularization)
* **Web Dashboard Engine:** Streamlit
* **Model Serialization:** Pickle

### Model Evaluation Profile
The performance metrics captured during training and validation checkpoints indicate high accuracy:
* **Linear Regression Training Error Score (R²):** `~0.8636`
* **Linear Regression Validation Error Score (R²):** `~0.8366`

---

## 📁 Repository Structure
```text
├── CAR_PRICE_PREDICTION.ipynb   # Jupyter Notebook containing EDA, pre-processing, and training pipelines
├── app_car.py                  # Main standalone styled Streamlit web application deployment file
├── car_price_model.pkl         # Serialized and trained Linear Regression model artifact
└── requirements.txt            # Python dependencies configuration for the deployment server environment
