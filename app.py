import streamlit as st
import pandas as pd
import joblib

# Load the newly trained model
loaded_model = joblib.load('trained_model.pkl')

# Streamlit app
st.set_page_config(page_title="Weather Data Prediction", layout="wide")
st.title("Weather Data Prediction App")

# Create a container for input fields with two columns
with st.container():
    st.header("Input Weather Data")

    col1, col2 = st.columns(2)

    with col1:
        mean_temp = st.number_input('Mean Temperature (°C)', value=25.0)
        max_temp = st.number_input('Maximum Temperature (°C)', value=30.0)
        min_temp = st.number_input('Minimum Temperature (°C)', value=20.0)
        dew_point = st.number_input('Dew Point (°C)', value=15.0)
        humidity = st.number_input('Humidity (%)', value=60.0)

    with col2:
        pressure = st.number_input('Sea Level Pressure (hPa)', value=1013.0)
        visibility = st.number_input('Visibility (km)', value=10.0)
        wind_speed = st.number_input('Wind Speed (m/s)', value=5.0)
        precipitation = st.number_input('Precipitation (mm)', value=0.0)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'Mean Temperature (°C)': [mean_temp],
    'Maximum Temperature (°C)': [max_temp],
    'Minimum Temperature (°C)': [min_temp],
    'Dew Point (°C)': [dew_point],
    'Humidity (%)': [humidity],
    'Sea Level Pressure (hPa)': [pressure],
    'Visibility (km)': [visibility],
    'Wind Speed (m/s)': [wind_speed],
    'Precipitation (mm)': [precipitation]
})

# Show input data
st.subheader("Input Data")
st.write(input_data)

# Predict and show result
if st.button('Predict'):
    try:
        prediction = loaded_model.predict(input_data)
        st.subheader("Prediction")
        st.write(f"Predicted value: {prediction[0]}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
