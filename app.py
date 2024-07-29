import streamlit as st
import pandas as pd
import joblib

# Load the newly trained model
loaded_model = joblib.load('trained_model.pkl')

# Streamlit app configuration
st.set_page_config(page_title="Weather Data Prediction", layout="wide")

# Custom CSS to style the app with a background image
st.markdown("""
    <style>
    .main {
        background: url('https://cdn.zeebiz.com/sites/default/files/2023/07/04/249475-delhi-weather-today-rain.jpg') no-repeat center center fixed;
        -webkit-background-size: cover;
        -moz-background-size: cover;
        -o-background-size: cover;
        background-size: cover;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2 {
        color: #f0f0f0;
        text-shadow: 2px 2px 4px #000000;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #4b2e83;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #6a46a1;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and description
st.title("🌤️ Weather Data Prediction App")
st.markdown("Use the sliders in the sidebar to input weather data, then click **Predict** to see the forecasted value.")

# Sidebar for input fields
st.sidebar.header("Input Weather Data")

mean_temp = st.sidebar.slider('Mean Temperature (°C)', min_value=-50.0, max_value=50.0, value=25.0, step=0.1)
max_temp = st.sidebar.slider('Maximum Temperature (°C)', min_value=-50.0, max_value=50.0, value=30.0, step=0.1)
min_temp = st.sidebar.slider('Minimum Temperature (°C)', min_value=-50.0, max_value=50.0, value=20.0, step=0.1)
dew_point = st.sidebar.slider('Dew Point (°C)', min_value=-50.0, max_value=50.0, value=15.0, step=0.1)
humidity = st.sidebar.slider('Humidity (%)', min_value=0.0, max_value=100.0, value=60.0, step=1.0)
pressure = st.sidebar.slider('Sea Level Pressure (hPa)', min_value=900.0, max_value=1100.0, value=1013.0, step=0.1)
visibility = st.sidebar.slider('Visibility (km)', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
wind_speed = st.sidebar.slider('Wind Speed (m/s)', min_value=0.0, max_value=50.0, value=5.0, step=0.1)
precipitation = st.sidebar.slider('Precipitation (mm)', min_value=0.0, max_value=500.0, value=0.0, step=0.1)

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
