from secrets import key1, key2, contacts
from twilio.rest import Client


class TwilioTextMessenger:
    def __init__(self):
        self.contacts = dict(contacts)
        self.twilio_number = contacts['My_Twilio']
        self.client = Client(key1, key2)

    def send(self, to_who, text_body):
        if to_who in contacts.keys():
            self.client.messages.create(to=self.contacts[to_who], from_=self.twilio_number, body=text_body)
        else:
            print('{} is not in your contacts in your secrets.py file'.format(to_who))
