import boto3
from secrets import *

client = boto3.client(
    'lambda', 'us-west-2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
function_name = 'send-text'
client.delete_function(FunctionName=function_name)

with open('text.zip', 'rb') as zip_file:
    zipfile = zip_file.read()

lambda_data = {
    'FunctionName': function_name,
    'Runtime': 'python3.6',
    'Role': 'arn:aws:iam::904892081344:role/service-role/Send_Message',
    'Handler': 'send_girlfriend_text.handler()',
    'Code': {
        'ZipFile': zipfile
    }
}

response = client.create_function(**lambda_data)

print(response)