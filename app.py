import streamlit as st
import pandas as pd
import joblib

# Load the trained model
loaded_model = joblib.load('trained_model.pkl')

# Define background images for different weather conditions
background_images = {
    "Clear": "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/green-field-over-blue-clear-sky-da-kuk.jpg",
    "Rain": "https://hhsmedia.com/wp-content/uploads/2019/06/rain-3964186_960_720-900x600.jpg",
    "Snow": "https://nsidc.org/sites/default/files/images/adam-chang-IWenq-4JHqo-unsplash.jpg",
    "Cloudy": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp-WDgraYvKZXTxAz0r-S85A5YVcGZ4z0p4w&s"
}

# Default background image
default_background = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/green-field-over-blue-clear-sky-da-kuk.jpg"

# Function to set background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Streamlit app configuration
st.set_page_config(page_title="Weather Data Prediction", layout="wide")
st.title("Weather Data Prediction App")

# Create a container for input fields with two columns
with st.container():
    st.header("Input Weather Data")
    
    col1, col2 = st.columns(2)

    # Column 1 for the first set of inputs
    with col1:
        mean_temp = st.slider('Mean Temperature (°C)', min_value=-50.0, max_value=50.0, value=25.0)
        max_temp = st.slider('Maximum Temperature (°C)', min_value=-50.0, max_value=50.0, value=30.0)
        min_temp = st.slider('Minimum Temperature (°C)', min_value=-50.0, max_value=50.0, value=20.0)
        dew_point = st.slider('Dew Point (°C)', min_value=-50.0, max_value=50.0, value=15.0)
        humidity = st.slider('Humidity (%)', min_value=0, max_value=100, value=60)

    # Column 2 for the second set of inputs
    with col2:
        pressure = st.slider('Sea Level Pressure (hPa)', min_value=950.0, max_value=1050.0, value=1013.0)
        visibility = st.slider('Visibility (km)', min_value=0.0, max_value=100.0, value=10.0)
        wind_speed = st.slider('Wind Speed (m/s)', min_value=0.0, max_value=50.0, value=5.0)
        precipitation = st.slider('Precipitation (mm)', min_value=0.0, max_value=500.0, value=0.0)

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

# Display input data
st.subheader("Input Data")
st.write(input_data)

# Predict and show result when the button is clicked
if st.button('Predict'):
    try:
        # Prediction using the loaded model
        prediction = loaded_model.predict(input_data)

        # Assume that the prediction output is a weather condition (e.g., "Clear", "Rain", etc.)
        weather_condition = prediction[0]  # Example: 'Clear'

        # Set the background image based on the weather condition
        background_image = background_images.get(weather_condition, default_background)
        set_background(background_image)

        st.subheader("Prediction")
        st.write(f"Predicted weather condition: {weather_condition}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
