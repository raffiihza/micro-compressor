from flask import Flask, request, jsonify
from flask_cors import CORS
import requests, os

app = Flask(__name__)
CORS(app)  # Mengaktifkan CORS untuk semua domain

API_KEY = os.environ.get('API_KEY', None)

@app.route('/', methods=['GET', 'HEAD'])
def health_check():
    return "The service is up"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    response = requests.get(weather_url)
    if response.status_code != 200:
        print(f"Error from API: {response.status_code} - {response.text}")
        return jsonify({'error': 'City not found'}), 404

    weather_data = response.json()
    return jsonify({
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))