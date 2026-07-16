import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ==============================
# Page Configuration
# ==============================

st.set_page_config(page_title="Crime Prediction", layout="wide")

st.title("🔮 Crime Category Prediction")
st.markdown("Predict the most likely crime category based on incident details.")

# ==============================
# Load Model Files
# ==============================

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "crime_model.pkl")
encoders = joblib.load(BASE_DIR / "feature_encoders.pkl")
target_encoder = joblib.load(BASE_DIR / "target_encoder.pkl")

st.subheader("Enter Crime Details")

col1, col2 = st.columns(2)

with col1:

    area = st.number_input("Area", min_value=1, value=1)

    area_name = st.selectbox(
        "Area Name",
        encoders["area name"].classes_
    )

    rpt_dist = st.number_input(
        "Report District No",
        min_value=1,
        value=100
    )

    part = st.selectbox(
        "Part 1-2",
        [1, 2]
    )

    crm_cd = st.number_input(
        "Crime Code",
        value=110
    )

    victim_age = st.slider(
        "Victim Age",
        0,
        100,
        25
    )

    victim_sex = st.selectbox(
        "Victim Sex",
        encoders["vict sex"].classes_
    )

    victim_descent = st.selectbox(
        "Victim Descent",
        encoders["vict descent"].classes_
    )

with col2:

    premis_cd = st.number_input(
        "Premise Code",
        value=101
    )

    premis_desc = st.selectbox(
        "Premise Description",
        encoders["premis desc"].classes_
    )

    weapon_cd = st.number_input(
        "Weapon Used Code",
        value=0
    )

    weapon_desc = st.selectbox(
        "Weapon Description",
        encoders["weapon desc"].classes_
    )

    status = st.selectbox(
        "Status",
        encoders["status"].classes_
    )

    status_desc = st.selectbox(
        "Status Description",
        encoders["status desc"].classes_
    )

    year = st.number_input(
        "Year",
        2020,
        2035,
        2024
    )

    month = st.slider(
        "Month",
        1,
        12,
        6
    )

    weekday = st.slider(
        "Weekday (0 = Monday)",
        0,
        6,
        2
    )

    hour = st.slider(
        "Hour",
        0,
        23,
        14
    )

    is_weekend = st.selectbox(
        "Weekend",
        [0, 1]
    )

    area_crime_count = st.number_input(
        "Area Crime Count",
        value=10000
    )
    # ==================================================
# Age Group
# ==================================================

age_young = 0
age_adult = 0
age_senior = 0

if 18 <= victim_age < 30:
    age_young = 1
elif 30 <= victim_age < 50:
    age_adult = 1
elif victim_age >= 50:
    age_senior = 1

# ==================================================
# Time Category
# ==================================================

morning = 0
afternoon = 0
evening = 0

if 6 <= hour < 12:
    morning = 1
elif 12 <= hour < 18:
    afternoon = 1
elif 18 <= hour < 24:
    evening = 1

# ==================================================
# Encode Categorical Features
# ==================================================

area_name = encoders["area name"].transform([area_name])[0]
victim_sex = encoders["vict sex"].transform([victim_sex])[0]
victim_descent = encoders["vict descent"].transform([victim_descent])[0]
premis_desc = encoders["premis desc"].transform([premis_desc])[0]
weapon_desc = encoders["weapon desc"].transform([weapon_desc])[0]
status = encoders["status"].transform([status])[0]
status_desc = encoders["status desc"].transform([status_desc])[0]

# ==================================================
# Prediction
# ==================================================

if st.button("🔮 Predict Crime"):

    sample = {

        "dr_no": 0,
        "area": area,
        "area name": area_name,
        "rpt dist no": rpt_dist,
        "part 1-2": part,
        "crm cd": crm_cd,
        "vict age": victim_age,
        "vict sex": victim_sex,
        "vict descent": victim_descent,
        "premis cd": premis_cd,
        "premis desc": premis_desc,
        "weapon used cd": weapon_cd,
        "weapon desc": weapon_desc,
        "status": status,
        "status desc": status_desc,
        "lat": 0,
        "lon": 0,
        "year": year,
        "month": month,
        "weekday": weekday,
        "hour": hour,
        "is_weekend": is_weekend,
        "area_crime_count": area_crime_count,

        "age_group_Young": age_young,
        "age_group_Adult": age_adult,
        "age_group_Senior": age_senior,

        "time_category_Morning": morning,
        "time_category_Afternoon": afternoon,
        "time_category_Evening": evening
    }

    # Convert to DataFrame
    data = pd.DataFrame([sample])

    # Match training column order
    prediction = model.predict(data)

    # Predict
    prediction = model.predict(data)

    # Decode prediction
    crime = target_encoder.inverse_transform(prediction)[0]

    # Display result
    st.success(f"🎯 Predicted Crime Category: **{crime}**")