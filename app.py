import streamlit as st
import requests

# Streamlit app configuration
st.set_page_config(page_title="Weather Data Prediction", layout="wide")

# Weatherbit API key (replace with your own API key)
API_KEY = "8fcb95aa406943989846fd4511f34d38"

# Define background images for different weather conditions
background_images = {
    "Clear": "https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/green-field-over-blue-clear-sky-da-kuk.jpg",
    "Rain": "https://hhsmedia.com/wp-content/uploads/2019/06/rain-3964186_960_720-900x600.jpg",
    "Snow": "https://nsidc.org/sites/default/files/images/adam-chang-IWenq-4JHqo-unsplash.jpg",
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
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set default background
set_background(default_background)

# App title and description
st.title("🌤️ Weather Data Prediction App")
st.markdown("Enter the city and country code, fetch the weather data, adjust the values using sliders, and predict the weather condition.")

# Sidebar for input fields
st.sidebar.header("Input Location")
city = st.sidebar.text_input('Enter City', value="KUTTIKANAM")
country = st.sidebar.text_input('Enter Country Code (e.g., IN)', value="IN")

# Fetch weather data from Weatherbit API
if st.sidebar.button('Get Weather Data'):
    try:
        url = f"https://api.weatherbit.io/v2.0/current?city={city}&country={country}&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        
        if 'data' in data:
            # Extract weather information
            weather = data['data'][0]
            temp = weather['temp']  # Temperature
            humidity = weather['rh']  # Humidity
            pressure = weather['pres']  # Pressure
            wind_speed = weather['wind_spd']  # Wind Speed
            weather_condition = weather['weather']['description']  # Weather description
            
            # Set background color using st.markdown with HTML and CSS
            st.markdown(f"""
                <div style="background-color: #e0e0e0; padding: 10px; border-radius: 10px;">
                    <h3 style="text-align: center;">Weather in {city}, {country}</h3>
                    <p>Current Weather Condition: {weather_condition}</p>
                    <p>Temperature: {temp} °C</p>
                    <p>Humidity: {humidity} %</p>
                    <p>Pressure: {pressure} hPa</p>
                    <p>Wind Speed: {wind_speed} m/s</p>
                </div>
            """, unsafe_allow_html=True)

            
            # Sliders to adjust values in the sidebar
            adjusted_temp = st.sidebar.slider("Temperature (°C)", min_value=-50, max_value=50, value=int(temp))
            adjusted_humidity = st.sidebar.slider("Humidity (%)", min_value=0, max_value=100, value=int(humidity))
            adjusted_pressure = st.sidebar.slider("Pressure (hPa)", min_value=900, max_value=1100, value=int(pressure))
            adjusted_wind_speed = st.sidebar.slider("Wind Speed (m/s)", min_value=0, max_value=50, value=int(wind_speed))
            
            if st.sidebar.button('Predict Weather Condition'):
                # Simple logic to predict weather based on user-adjusted values
                if adjusted_temp > 30 and adjusted_humidity < 40:
                    predicted_condition = "Clear"
                elif adjusted_humidity > 80 and adjusted_wind_speed > 10:
                    predicted_condition = "Rain"
                elif adjusted_temp < 0:
                    predicted_condition = "Snow"
                else:
                    predicted_condition = "Cloudy"
                
                st.subheader(f"Predicted Weather Condition: {predicted_condition}")
                
                # Change background based on predicted condition
                set_background(background_images.get(predicted_condition, default_background))
        else:
            st.error("Could not fetch weather data. Please check the city or country code.")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Additional information on Weatherbit API
st.markdown("""
    **Note:** Ensure that the city and country code are valid.
""")
