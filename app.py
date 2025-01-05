from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = <your-api-key>

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        return render_template('index.html', error="City name cannot be empty.")
    
    # OpenWeatherMap API URLs
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    current_response = requests.get(current_weather_url)
    forecast_response = requests.get(forecast_url)
    
    if current_response.status_code == 200 and forecast_response.status_code == 200:
        current_data = current_response.json()
        forecast_data = forecast_response.json()

        # Current weather
        weather_info = {
            "city": current_data["name"],
            "country": current_data["sys"]["country"],
            "temperature": current_data["main"]["temp"],
            "feels_like": current_data["main"]["feels_like"],
            "humidity": current_data["main"]["humidity"],
            "weather": current_data["weather"][0]["description"].capitalize(),
            "icon": current_data["weather"][0]["icon"],
            "wind_speed": current_data["wind"]["speed"]
        }

        # Forecast (next 5 timeslots)
        forecast = [
            {
                "time": item["dt_txt"],
                "temp": item["main"]["temp"],
                "weather": item["weather"][0]["description"].capitalize(),
                "icon": item["weather"][0]["icon"],
                "wind_speed": item["wind"]["speed"]
            }
            for item in forecast_data["list"][:5]
        ]
        return render_template('index.html', weather=weather_info, forecast=forecast)
    else:
        return render_template('index.html', error="City not found. Please try again.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

