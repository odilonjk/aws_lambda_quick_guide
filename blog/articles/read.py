import json


def read_article(event, context):
    body = {
        "title": "How to use AWS Lambda",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc justo."
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
