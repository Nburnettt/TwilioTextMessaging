from twilio_text_messenger import TwilioTextMessenger
from secrets import girlfriend_name, city
from weather_grabber import WeatherGrabber
from compliment_generator import ComplimentGenerator


class GirlfriendTextMessenger(TwilioTextMessenger):
    def __init__(self):
        super().__init__()
        self.girlfriend_name = girlfriend_name
        self.girlfriend_city = city

    def send_girlfriend_text(self):
        name = "My_Cell"
        compliment = ComplimentGenerator.get_girlfriend_compliment()
        text_body = '-\r\rGood Morning {}!\r'.format(self.girlfriend_name) + compliment
        text_body += self.weather_update()
        self.send(name, text_body)

    def weather_update(self):
        high, low, average, description = WeatherGrabber(self.girlfriend_city).get_today()
        update = '\rP.S. Today will be {} and about {} degrees (high of {}, low of {}).'\
            .format(description, average, high, low)
        return update
