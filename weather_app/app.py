from flask import Flask, render_template, request

import requests

# Variables for application use;
url_link = "https://api.openweathermap.org/data/2.5/weather"
api_key = "503592691d958ea9d85a8496d6872978"
city_name = "tokyo"

# Application Parameters;
params = {
    "q": city_name,
    "appid": api_key,
    "units": "metric" 
}

# data = requests.get(url=url_link, params=params)
# data = data.json()

# Application;
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods= ['POST', 'GET'])
def get_weather_data():
    
    # Variables from Form;
    url_link = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "503592691d958ea9d85a8496d6872978"
    city_name = request.form.get('city')
    api_key = request.form.get('appid')
    
    # Parameters;
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" 
    }
    
    # return f"City Name {city_name}"
    response = requests.get(url=url_link, params=params)
    data = response.json()
    
    return f"data = {data}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8001", debug="True")