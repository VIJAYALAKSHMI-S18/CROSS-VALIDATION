import streamlit as st
import pandas as pd
import pickle

# Load model
with open("forestfire_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Forest Fire Prediction")

st.title("🔥 Forest Fire Burned Area Prediction")

# -------- Inputs --------
X = st.number_input("X Coordinate", value=7)
Y = st.number_input("Y Coordinate", value=5)

month = st.selectbox("Month", ["jan","feb","mar","apr","may","jun",
                               "jul","aug","sep","oct","nov","dec"])
day = st.selectbox("Day", ["mon","tue","wed","thu","fri","sat","sun"])

FFMC = st.number_input("FFMC", value=86.2)
DMC = st.number_input("DMC", value=26.2)
DC = st.number_input("DC", value=94.3)
ISI = st.number_input("ISI", value=5.1)

temp = st.number_input("Temperature (°C)", value=8.2)
RH = st.number_input("Relative Humidity (%)", value=51)
wind = st.number_input("Wind Speed", value=6.7)
rain = st.number_input("Rain (mm)", value=0.0)

# -------- Prediction --------
if st.button("Predict"):
    input_df = pd.DataFrame([{
        "X": X,
        "Y": Y,
        "month": month,
        "day": day,
        "FFMC": FFMC,
        "DMC": DMC,
        "DC": DC,
        "ISI": ISI,
        "temp": temp,
        "RH": RH,
        "wind": wind,
        "rain": rain
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"🔥 Burned Area: {prediction:.2f} hectares")
