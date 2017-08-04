from apixu.client import ApixuClient, ApixuException


class WeatherGrabber:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def get_today(self):
        client = ApixuClient(self.api_key)
        current = client.getForecastWeather(q=self.city, days=1)
        high = current['forecast']['forecastday'][0]['day']['maxtemp_f']
        low = current['forecast']['forecastday'][0]['day']['mintemp_f']
        average = current['forecast']['forecastday'][0]['day']['avgtemp_f']
        description = current['forecast']['forecastday'][0]['day']['condition']['text']
        return high, low, average, description

