import json
import boto3


def delete_article(event, context):
    article_id = event["article_id"]

    dynamodb = boto3.client("dynamodb")
    response = dynamodb.delete_item(
        TableName="BlogTable",
        Key={
            "article_id": {"S": str(article_id)}
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
