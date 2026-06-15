# 🏥 Medical Appointment No-Show Prediction & Demand Forecasting System

## 📌 Project Overview
This project is a healthcare analytics system that predicts whether a patient will miss an appointment and analyzes hospital demand patterns using machine learning and an interactive Streamlit dashboard.

The system helps hospitals reduce no-shows, improve scheduling efficiency, and optimize resource allocation.

---

## 🚀 Features

- Data Cleaning and Preprocessing
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Machine Learning Model for No-show Prediction
- Demand Forecasting Analysis
- Interactive Streamlit Dashboard with 3 modules:
  - Dashboard View
  - No-show Predictor
  - Demand Forecaster

---

## 📁 Project Structure

medical-appointment-no-show-prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── processed_medical_data.csv
│
├── notebooks/
│   └── eda.py
│
├── app/
│   └── app.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone <repository-link>
cd medical-appointment-no-show-prediction

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

### 3. Install dependencies
pip install -r requirements.txt

---

## ▶️ How to Run the Project

Run Streamlit application:
streamlit run app/app.py

Open in browser:
http://localhost:8501/

---

## 📊 Data Dictionary

| Column Name | Description |
|-------------|-------------|
| age | Age of the patient |
| specialty | Medical department |
| place | Hospital location |
| appointment_shift | Time of appointment |
| no_show | Target variable (1 = No-show, 0 = Show) |
| age_group | Age category (Child, Teen, Adult, etc.) |
| health_risk_score | Risk score based on health conditions |
| is_weekend_shift | Whether appointment is weekend shift |
| under_12_years_old | Child indicator |
| over_60_years_old | Senior indicator |
| patient_needs_companion | Assistance requirement |

---

## 📊 Dashboard Modules

### 1. Dashboard View
- Total patients
- No-show rate
- Age group distribution
- Specialty demand analysis

### 2. No-show Predictor
- User inputs patient details
- Model predicts attendance or absence

### 3. Demand Forecaster
- Specialty-wise demand
- Age group demand
- Location-based patient distribution

---

## 🧠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Plotly / Matplotlib

---

## 📌 Future Improvements

- Improve ML model accuracy with hyperparameter tuning
- Add time-series forecasting for demand prediction
- Deploy application on Streamlit Cloud or Render
- Add notification system for appointment reminders

---

## 👨‍💻 Author
Student Project – Medical Appointment Intelligence System