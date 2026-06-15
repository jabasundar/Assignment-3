import streamlit as st
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Medical Intelligence System", layout="wide")

st.title("🏥 Medical Appointment Intelligence System")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "processed", "processed_medical_data.csv")
    return pd.read_csv(file_path)

df = load_data()

# ---------------- MODEL TRAINING ----------------
features = [
    "age",
    "health_risk_score",
    "is_weekend_shift",
    "specialty",
    "place",
    "age_group"
]

target = "no_show"

X = df[features]
y = df[target]

X = pd.get_dummies(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "🤖 No-Show Predictor",
    "📈 Demand Forecaster"
])

# ---------------- DASHBOARD ----------------
with tab1:
    st.subheader("📊 Overview Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Patients", len(df))
    col2.metric("No-Show Rate (%)", round(df["no_show"].mean() * 100, 2))
    col3.metric("Total No-Shows", df["no_show"].sum())
    st.markdown("### 👥 Patient Age Group Distribution")
    st.bar_chart(df["age_group"].value_counts())
    st.markdown("### 🏥 Department (Specialty) Demand")
    st.bar_chart(df["specialty"].value_counts())

# ---------------- PREDICTOR ----------------
with tab2:
    st.subheader("🤖 No-Show Prediction")

    age = st.number_input("Age", 0, 100, 25)
    risk = st.number_input("Health Risk Score", 0, 10, 2)
    weekend = st.selectbox("Is Weekend Shift?", [0, 1])
    specialty = st.selectbox("Specialty", df["specialty"].unique())
    place = st.selectbox("Place", df["place"].unique())
    age_group = st.selectbox("Age Group", df["age_group"].unique())

    input_data = pd.DataFrame([[
        age, risk, weekend, specialty, place, age_group
    ]], columns=features)

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=X.columns, fill_value=0)

    if st.button("Predict No-Show"):
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠ Patient is likely to MISS appointment")
        else:
            st.success("✅ Patient is likely to ATTEND appointment")

# ---------------- DEMAND FORECASTER ----------------
with tab3:
    st.subheader("📈 Demand Forecaster")

    st.write("📌 Specialty-wise demand")
    st.bar_chart(df["specialty"].value_counts())

    st.write("📌 Age group demand")
    st.bar_chart(df["age_group"].value_counts())

    st.write("📌 Place-wise demand")
    st.bar_chart(df["place"].value_counts())

    st.info("This helps hospitals plan doctors, staff, and scheduling.")