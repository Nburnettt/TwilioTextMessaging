from apixu.client import ApixuClient, ApixuException
from urllib import request
import ast

class WeatherGrabber:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def get_today(self):
        client = ApixuClient(self.api_key)
        url = 'https://api.apixu.com/v1/forecast.json?key={}&q={}'.format(self.api_key, self.city)
        response = request.urlopen(url).read().decode('utf-8')
        current = ast.literal_eval(response)
        high = current['forecast']['forecastday'][0]['day']['maxtemp_f']
        low = current['forecast']['forecastday'][0]['day']['mintemp_f']
        average = current['forecast']['forecastday'][0]['day']['avgtemp_f']
        description = current['forecast']['forecastday'][0]['day']['condition']['text']
        return high, low, average, description

