from __future__ import print_function
import json
import boto3
import decimal
import uuid


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


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

    response = {
        "statusCode": 200,
        "body": json.dumps(response, indent=4, cls=DecimalEncoder)
    }

    return response


def validate_text(text):
    if not isinstance(text, str):
        raise TypeError("Text property should be of text type.")
    if not text.strip():
        raise ValueError("Text property should not be empty.")
