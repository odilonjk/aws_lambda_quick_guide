import json


def hello(event, context):
    remaining_time = context.get_remaining_time_in_millis()
    print("Event: {}\nRemaining time: {}".format(event, remaining_time))

    body = {
        "message": "Hello world! That's a very simple example of lambda function!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
