from helper.TextHelper import validate_text
import boto3
import json


def update_article(event, context):
    article_id = event["article_id"]
    title = event["title"]
    text = event["text"]

    validate_text(title)
    validate_text(text)

    dynamodb = boto3.client("dynamodb")
    response = dynamodb.update_item(
        TableName="BlogTable",
        Key={
            "article_id": {"S": str(article_id)}
        },
        AttributeUpdates={
            "title": {"Action": "PUT", "Value": {"S": title}},
            "text": {"Action": "PUT", "Value": {"S": text}}
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
