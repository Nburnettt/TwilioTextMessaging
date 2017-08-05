from lib_twilio_text_messenger import TwilioTextMessenger
from lib_weather_grabber import WeatherGrabber
from lib_compliment_generator import ComplimentGenerator


class GirlfriendTextMessenger(TwilioTextMessenger):
    def __init__(self, **kwargs):
        self.girlfriend_name = kwargs.pop('girlfriend_name')
        self.girlfriend_city = kwargs.pop('city')
        self.apixu_api_key = kwargs.pop('apixu_api_key')
        super().__init__(**kwargs)

    def send_girlfriend_text(self):
        compliment = ComplimentGenerator.get_girlfriend_compliment()
        text_body = '-\r\rGood Morning {}!\r'.format(self.girlfriend_name) + compliment
        text_body += self.weather_update()
        self.send_https(self.girlfriend_name, text_body)

    def weather_update(self):
        high, low, average, description = WeatherGrabber(self.apixu_api_key, self.girlfriend_city).get_today()
        update = '\rP.S. Today will be {} and about {} degrees (high of {}, low of {}).'\
            .format(description, average, high, low)
        return update
