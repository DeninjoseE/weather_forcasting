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
        mean_temp = st.slider('Mean Temperature (°C)', min_value=-50.0, max_value=50.0, value=25.0, step=0.1)
        max_temp = st.slider('Maximum Temperature (°C)', min_value=-50.0, max_value=50.0, value=30.0, step=0.1)
        min_temp = st.slider('Minimum Temperature (°C)', min_value=-50.0, max_value=50.0, value=20.0, step=0.1)
        dew_point = st.slider('Dew Point (°C)', min_value=-50.0, max_value=50.0, value=15.0, step=0.1)
        humidity = st.slider('Humidity (%)', min_value=0.0, max_value=100.0, value=60.0, step=1.0)

    with col2:
        pressure = st.slider('Sea Level Pressure (hPa)', min_value=900.0, max_value=1100.0, value=1013.0, step=0.1)
        visibility = st.slider('Visibility (km)', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
        wind_speed = st.slider('Wind Speed (m/s)', min_value=0.0, max_value=50.0, value=5.0, step=0.1)
        precipitation = st.slider('Precipitation (mm)', min_value=0.0, max_value=500.0, value=0.0, step=0.1)

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
