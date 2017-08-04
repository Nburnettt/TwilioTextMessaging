from helper_library.twilio_text_messenger import TwilioTextMessenger
from helper_library.weather_grabber import WeatherGrabber
from helper_library.compliment_generator import ComplimentGenerator


class GirlfriendTextMessenger(TwilioTextMessenger):
    def __init__(self, **kwargs):
        self.girlfriend_name = kwargs.pop('girlfriend_name')
        self.girlfriend_city = kwargs.pop('city')
        self.apixu_api_key = kwargs.pop('apixu_api_key')
        super().__init__(**kwargs)

    def send_girlfriend_text(self):
        name = "My_Cell"
        compliment = ComplimentGenerator.get_girlfriend_compliment()
        text_body = '-\r\rGood Morning {}!\r'.format(self.girlfriend_name) + compliment
        text_body += self.weather_update()
        self.send(name, text_body)

    def weather_update(self):
        high, low, average, description = WeatherGrabber(self.apixu_api_key, self.girlfriend_city).get_today()
        update = '\rP.S. Today will be {} and about {} degrees (high of {}, low of {}).'\
            .format(description, average, high, low)
        return update
