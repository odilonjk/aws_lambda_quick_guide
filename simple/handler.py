import json


def hello(event, context):
    body = {
        "message": "Hello world! That's a very simple example of lambda function!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
