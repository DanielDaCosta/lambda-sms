# lambda-sms

Lambda that sends sms to user, built using Terraform. It receives an array of dictionaries containing
phone_number and message.

Lamba event input:

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

This modules reads all its Secure Credentials form AWS Systems Manager Parameter Store, as it can be seen in the file *config.py*

## Example of lambda call .

Lambda *asynchronous invocation* is preferable

```
import json
import boto3
from config import MS_SMS

# MS_SMS = "name_of_function"


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

## Calling module

```
# Module 
module "sms" 
    source = "{git@github.com:DanielDaCosta/lambda-sms.git"

    lambda_name             = var.lambda_sms
    environment             = var.environment
    name                    = var.name
    region                  = var.region
}
```
