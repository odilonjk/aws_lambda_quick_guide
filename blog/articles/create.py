from __future__ import print_function
from helper.TextHelper import validate_text
import json
import boto3
import decimal
import uuid


def create_article(event, context):
    title = event["title"]
    text = event["text"]

    validate_text(title)
    validate_text(text)

    dynamodb = boto3.client("dynamodb")

    response = dynamodb.put_item(
        TableName="BlogTable",
        Item={
            "article_id": {"S": str(uuid.uuid4())},
            "title": {"S": title},
            "text": {"S": text}
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
