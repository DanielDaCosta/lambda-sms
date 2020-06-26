# lambda-sms

Lambda that sends sms to user. It receives an array of dictionaries containing
phone_number and message.
Input:

```
{
    "data": {
        [
            {
                'phone_number': '+552199999999',
                'message': 'Bom dia!'
            },
            {
                'phone_number': '+5521991299889',
                'message': 'Bom tarde!'
            }
        ]
    }
}
```

# Usage

Example of usage.

Lambda *asynchronous invocation* is preferable

```
import json
import boto3
from config import MS_SMS

# MS_SMS = "risk-mg-platform-dev-sms"


def send_sms(messages_array):
    """Send sms
    Args:
        phone_number (string): the phone number that will receive the sms
        body_message (string): the message
    """
    client = boto3.client('lambda')
    payload = {
        "data": messages_array
    }
    client.invoke(
        FunctionName=MS_SMS,
        InvocationType='Event',
        Payload=json.dumps(payload),
        LogType='None'
    )

```