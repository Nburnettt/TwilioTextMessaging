from twilio.rest import Client


class TwilioTextMessenger:
    def __init__(self, **kwargs):
        self.contacts = dict(kwargs.pop('contacts'))
        self.twilio_number = self.contacts['My_Twilio']
        key_1 = kwargs.pop('twilio_key_1')
        key_2 = kwargs.pop('twilio_key_2')
        self.client = Client(key_1, key_2)

    def send(self, to_who, text_body):
        if to_who in self.contacts.keys():
            self.client.messages.create(to=self.contacts[to_who], from_=self.twilio_number, body=text_body)
        else:
            print('{} is not in your contacts in your secrets.py file'.format(to_who))
