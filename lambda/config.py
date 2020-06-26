from os import getenv
import boto3

ssm = boto3.client("ssm")

environment = getenv("ENV")

path = '/{}/general'.format(environment)

TWILIO_ACCOUNT_SID = ssm.get_parameter(
    Name='{}/TWILIO_ACCOUNT_SID'.format(path),
    WithDecryption=True,
)['Parameter']['Value']

TWILIO_AUTH_TOKEN = ssm.get_parameter(
    Name='{}/TWILIO_AUTH_TOKEN'.format(path),
    WithDecryption=True,
)['Parameter']['Value']

TWILIO_PHONE_NUMBER = ssm.get_parameter(
    Name='{}/TWILIO_PHONE_NUMBER'.format(path),
    WithDecryption=True,
)['Parameter']['Value']
