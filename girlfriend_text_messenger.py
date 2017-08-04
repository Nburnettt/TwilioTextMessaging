from twilio_text_messenger import TwilioTextMessenger
from secrets import girlfriend_name
import random
import requests


class GirlfriendTextMessenger(TwilioTextMessenger):
    def __init__(self):
        super().__init__()
        self.girlfriend_name = girlfriend_name

    def send_girlfriend_text(self):
        name = "My_Cell"
        random.seed(None)
        x = random.randint(1,18)
        comps = open("compliments.txt", "r")
        for i in range(x):
            compliment = comps.readline()
        text_body = '-\r\rGood Morning {}!\r' + name
        r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20item.forecast%20from%20weather.forecast%20where%20woeid%20in%20(2385382)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
        data = r.json()
        high = data['query']['results']['channel'][0]['item']['forecast']['high']
        low = data['query']['results']['channel'][0]['item']['forecast']['low']
        details = data['query']['results']['channel'][0]['item']['forecast']['text']
        text_body += "\rP.S. Today will be " + details + " with a high of " + high + " and a low of " + low + ". "
        self.send(name, text_body)
