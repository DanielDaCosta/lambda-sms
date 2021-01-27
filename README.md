# Sending SMS in AWS Lambda with Twilio API

Lambda that sends sms to user using Twilio API. It receives an array of dictionaries containing
phone_number and message.

Lamba *event* input:

```
{
    "data": {
        [
            {
                'phone_number': '+552199999999',
                'message': 'Good Morning!'
            },
            {
                'phone_number': '+5521991299889',
                'message': 'Good Afternoon!'
            },
            {
                'phone_number': '+5521912412997',
                'message': 'Good Night!'
            }
        ]
    }
}
```
# Details

The repository already contains the required Twillio 6.4.0 package installed inside the *package* folder

# Usage

This modules reads all its Secure Credentials from AWS Systems Manager Parameter Store, as it can be seen in the file *config.py*.

For the *twilio credentials*, you can create your free account in their website: https://www.twilio.com 

## Example of lambda invoke

Lambda *asynchronous invocation* is preferable

```python
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

## Importing Terraform module

```terraform
# Module 
module "sms" 
    source = "git@github.com:DanielDaCosta/lambda-sms.git"

    lambda_name             = var.lambda_sms
    environment             = var.environment
    name                    = var.name
    region                  = var.region
}
```
