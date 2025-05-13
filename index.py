import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("WebFormSubmissions")

def lambda_handler(event, context):
    data = json.loads(event["body"])
    submission_id = str(uuid.uuid4())

    item = {
        "submissionId": submission_id,
        "name": data["name"],
        "email": data["email"],
        "message": data["message"]
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({"message": "Form submitted successfully!"})
    }
