import streamlit as st
import pandas as pd
import joblib
import os

def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "app/style.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css()

st.title('🚆 Smart Railway Resource Planning Dashboard')

df = pd.read_csv("../data/railway_data.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Passenger Distribution")

st.bar_chart(df["passenger_count"])

model = joblib.load("../models/delay_model.pkl")

st.sidebar.header("Train Inputs")

arrival = st.sidebar.slider("Arrival Hour",0,23)
departure = st.sidebar.slider("Departure Hour",0,23)
passengers = st.sidebar.number_input("Passenger Count",100,2000)
platform = st.sidebar.slider("Platform Number",1,6)
track = st.sidebar.slider("Track Number",1,4)

if st.sidebar.button("Predict Delay"):

    data = [[arrival,departure,passengers,platform,track]]

    prediction = model.predict(data)

    st.success(f"Predicted Delay: {prediction[0]:.2f} minutes")

st.subheader("Train Traffic by Hour")

traffic = df.groupby("arrival_hour").size()

st.line_chart(traffic)

st.subheader("Platform Usage")

platform_usage = df["platform_number"].value_counts()

st.bar_chart(platform_usage)