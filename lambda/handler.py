import sys
sys.path.insert(0, 'package/')
import json
import logging
from twilio.rest import Client
from config import \
    TWILIO_ACCOUNT_SID, \
    TWILIO_AUTH_TOKEN, \
    TWILIO_PHONE_NUMBER
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send_sms(phone_number, body_message):
    """Send sms
    Args:
        phone_number (string): the phone number that will receive the sms
        body_message (string): the message
    """

    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    try:
        client = Client(account_sid, auth_token)

        client.messages.create(
            body=body_message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        logger.info("send_sms: Message sent to number: %s" % (phone_number))
    except Exception as err:
        logging.error("send_sms: Message not sent to %s"
                      % (phone_number))
        raise Exception(err)


def lambda_handler(event, context):
    for message in event['data']:
        phone_number = message['phone_number']
        body_message = message['message']
        send_sms(phone_number, body_message)
