import streamlit as st
import pandas as pd
import joblib
import os


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

# Check platform conflict
conflict = df[
    (df["platform_number"] == platform) &
    (df["arrival_hour"] == arrival)
]

if len(conflict) > 0:
    st.warning("⚠ Platform Conflict Detected!")

    free_platforms = list(set(range(1,7)) - set(df["platform_number"]))

    if len(free_platforms) > 0:
        st.info(f"Suggested Free Platform: {free_platforms[0]}")
    else:
        st.error("No platforms available at this time")

if st.sidebar.button("Predict Delay"):

    # Conflict detection
    conflict = df[
        (df["platform_number"] == platform) &
        (df["arrival_hour"] == arrival)
    ]

    if len(conflict) > 0:
        st.warning("⚠ Platform Conflict Detected!")

    data = [[arrival,departure,passengers,platform,track]]

    prediction = model.predict(data)

    st.success(f"Predicted Delay: {prediction[0]:.2f} minutes")

st.subheader("Train Traffic by Hour")

traffic = df.groupby("arrival_hour").size()
st.line_chart(traffic)

st.subheader("Platform Usage")

platform_usage = df["platform_number"].value_counts()
st.bar_chart(platform_usage)