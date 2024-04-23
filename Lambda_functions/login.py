import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    email = event["email"]
    password = event["password"]
    client = boto3.resource("dynamodb")
    table = client.Table("login")
    search = table.query(KeyConditionExpression=Key("email").eq(email))["Items"]
    if (search[0]['email'] == email and search[0]['password'] == password):
               resp = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
            },
            "body": {"Result": "login successful","username":search[0]['user_name']},
        }
    else:
                resp = {
            "statusCode": 400,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
            },
            "body": {"Result": "login failed"},
        }
    return resp

    