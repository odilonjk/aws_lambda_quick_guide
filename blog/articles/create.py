import json


def create_article(event, context):
    text = event["text"]
    if not isinstance(text, str):
        raise TypeError("Text property should be of text type.")
    if not text.strip():
        raise ValueError("Text property should not be empty.")
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Article created with success!"})
    }

    return response
