from girlfriend_text_messenger import GirlfriendTextMessenger
from secrets import *

kwargs = {'contacts': contacts,
          'girlfriend_name': 'My_Cell',
          'city': city,
          'twilio_key_1': key1,
          'twilio_key_2': key2,
          'apixu_api_key': apixu_api_key
          }


def handler():
    GirlfriendTextMessenger(**kwargs).send_girlfriend_text()

if __name__ == '__main__':
    handler()