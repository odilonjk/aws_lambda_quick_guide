import json


def update_article(event, context):

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Article updated with success!"})
    }

    return response
