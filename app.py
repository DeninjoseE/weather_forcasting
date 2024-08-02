import streamlit as st
import pandas as pd
import joblib
import io

# Load the trained model
loaded_model = joblib.load('trained_model.pkl')

# Streamlit app configuration
st.set_page_config(page_title="Weather Data Prediction", layout="wide")

# Define background images for different weather conditions
background_images = {
    "Clear": "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/green-field-over-blue-clear-sky-da-kuk.jpg",
    "Rain": "https://hhsmedia.com/wp-content/uploads/2019/06/rain-3964186_960_720-900x600.jpg",
    "Snow": "https://imageio.forbes.com/specials-images/imageserve/639c5cdcb6175432cb9a89d7/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds",
    "Cloudy": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp-WDgraYvKZXTxAz0r-S85A5YVcGZ4z0p4w&s"
}

# Default background image
default_background = "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/green-field-over-blue-clear-sky-da-kuk.jpg"

# Function to set the background image based on the weather condition
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .main {{
            background: url('{image_url}') no-repeat center center fixed;
            -webkit-background-size: cover;
            -moz-background-size: cover;
            -o-background-size: cover;
            background-size: cover;
            color: #ffffff;
        }}
        .sidebar .sidebar-content {{
            background-color: rgba(255, 255, 255, 0.7);
            padding: 20px;
            border-radius: 10px;
        }}
        h1, h2 {{
            color: #f0f0f0;
            text-shadow: 2px 2px 4px #000000;
        }}
        .stButton>button {{
            color: #ffffff;
            background-color: #4b2e83;
            border-radius: 5px;
            padding: 10px 20px;
        }}
        .stButton>button:hover {{
            background-color: #6a46a1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set default background
set_background(default_background)

# App title and description
st.title("🌤️ Weather Data Prediction App")
st.markdown("Use the sliders in the sidebar to input weather data, then click **Predict** to see the forecasted value.")

# Sidebar for input fields
st.sidebar.header("Input Weather Data")

# Collect user input through sliders
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
        weather_condition = prediction[0]  # Assuming the model predicts the weather condition directly
        st.markdown(f"<h2 style='color: white;'>Prediction</h2>", unsafe_allow_html=True)
        st.markdown(f"<span style='color: white; font-weight: bold;'>Predicted value: {weather_condition}</span>", unsafe_allow_html=True)
        set_background(background_images.get(weather_condition, default_background))
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Test data
test_data_csv = """
Mean Temperature (°C),Maximum Temperature (°C),Minimum Temperature (°C),Dew Point (°C),Humidity (%),Sea Level Pressure (hPa),Visibility (km),Wind Speed (m/s),Precipitation (mm),Weather Condition
6.9,21.2,-4.1,8.9,32.5,990.9,1.3,13,60.1,Snow
21.9,22.2,7.4,18.3,37,992.7,3.7,4.6,52.5,Rain
9.4,13.8,0.2,-9.4,43.4,1005.6,9.2,11.8,20,Clear
13.1,22,12.4,9.3,33.6,984.6,19,14.5,80.8,Clear
3.7,5.2,-6.6,2.6,29.8,1014.7,0.8,13.6,25.9,Rain
19.8,24.5,12,6.9,34.8,1047.9,15.5,14.1,89.5,Clear
16.9,30.7,15.6,15.6,23.6,1002.8,7.8,4.1,82.9,Cloudy
6.1,10.3,-2,-9.4,84.2,985.2,19.7,11.6,19.9,Snow
-9.8,2.4,-20.4,14.2,81.7,985.2,7.2,1.7,86.3,Cloudy
18,23,17,-2.6,46,1031.1,12.8,13.3,47.2,Rain
-4.6,6.1,-16,7.5,81.7,1014.6,10.5,6.4,2.5,Clear
-5.1,-4.6,-14.6,-2.4,60.7,1043.5,5.1,6.2,75.6,Clear
0.3,1.5,-4,-8.6,94.4,1036.6,12.7,13.1,80.4,Snow
-1.6,11.8,-9.7,17.3,91.7,1002.3,2.3,3.4,42.7,Clear
26.8,39.7,26.7,5.4,53.4,995.5,2.5,5.1,94.3,Snow
4.5,12.3,-6,-0.5,97.7,1047.4,5.1,7.5,30.1,Rain
2.8,3.4,-6.3,5.1,24.1,999.5,18.2,3.6,14.5,Rain
12,26.8,8.4,11.9,80.9,996.6,14.6,5.5,63.2,Rain
"""

# Convert the CSV string to a DataFrame
test_data = pd.read_csv(io.StringIO(test_data_csv))

# Initialize the session state to track visibility
if 'show_test_data' not in st.session_state:
    st.session_state.show_test_data = False

# Button to show/hide test data
if st.button('Toggle Test Data'):
    st.session_state.show_test_data = not st.session_state.show_test_data

# Display test data if toggled
if st.session_state.show_test_data:
    st.subheader("Test Data")
    st.write(test_data)
else:
    st.markdown("""
    <p style='color: #FFFFFF; font-weight: bold;'>
        <span style='color: #FF0000; font-weight: bold;'>NB: </span> Click the <span style='color: #FF0000; font-weight: bold;'>**Toggle Test Data**</span> button to view the test data. 
        You can use this data as a reference or input your own custom data points using the sliders in the sidebar.
    </p>
    """, unsafe_allow_html=True)
