import requests

def get_weather(city):
    url = 'http://api.weatherapi.com/v1/current.json'
    params = {'key': '6580ce5f3a1b414d80b134352221912', 'q': {city}, 'aqi': 'no'}

    return requests.get(url, params).json().get('current').get('temp_c')