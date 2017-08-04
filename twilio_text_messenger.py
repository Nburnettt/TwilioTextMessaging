import random
import yweather
import requests
from secrets import key1, key2, contacts
from twilio.rest import Client


class TwilioTextMessenger:
    def __init__(self):
        self.contacts = dict(contacts)
        self.twilio_number = contacts['My_Twilio']
        self.client = Client(key1, key2)

    def girlfriend_text(self):
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

    def send(self, to_who, text_body):
        if to_who in contacts.keys():
            self.client.messages.create(to=self.contacts[to_who], from_=self.twilio_number, body=text_body)
        else:
            print('{} is not in your contacts in your secrets.py file'.format(to_who))
