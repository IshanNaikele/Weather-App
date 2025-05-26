# app.py
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # For session security
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temp': round(data['main']['temp'], 1),
            'feels_like': round(data['main']['feels_like'], 1),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': round(data['wind']['speed'] * 3.6, 1),
            'wind_deg': data['wind'].get('deg', None),
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'visibility': data.get('visibility', None),
            'timestamp': datetime.fromtimestamp(data['dt']).strftime('%a %H:%M')
        }
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None
    except KeyError as e:
        print(f"Data parsing error: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if not city:
            error = "Please enter a city name"
        else:
            weather_data = get_weather_data(city)
            if not weather_data:
                error = "City not found or API error. Please try again."
    
    return render_template('index.html', 
                         weather=weather_data, 
                         error=error,
                         timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    app.run(debug=False)  # Always set debug=False in production