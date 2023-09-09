import requests

def get_humidity(latitude, longitude, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        humidity = data['main']['humidity']
        return humidity
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example usage:
api_key = "3aef63c856eeb24c8b3f980d307464d4" 
latitude = 40.730610
longitude = -73.935242
humidity = get_humidity(latitude, longitude, api_key)
if humidity is not None:
    print(f"The humidity at the coordinates ({latitude}, {longitude}) is: {humidity}%")
