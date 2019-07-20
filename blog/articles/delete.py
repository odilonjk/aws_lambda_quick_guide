import json


def delete_article(event, context):

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Article deleted with success!"})
    }

    return response
