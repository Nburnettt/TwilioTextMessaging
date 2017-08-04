from apixu.client import ApixuClient, ApixuException
from secrets import api_key


class WeatherGrabber:
    def __init__(self, city):
        self.city = city

    def get_today(self):
        client = ApixuClient(api_key)
        current = client.getForecastWeather(q=self.city, days=1)
        high = current['forecast']['forecastday'][0]['day']['maxtemp_f']
        low = current['forecast']['forecastday'][0]['day']['mintemp_f']
        average = current['forecast']['forecastday'][0]['day']['avgtemp_f']
        description = current['forecast']['forecastday'][0]['day']['condition']['text']
        return high, low, average, description

