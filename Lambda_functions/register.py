import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    type = event["type"]
    email = event["email"]
    username = event["username"]
    password = event["password"]
    # this will create dynamodb resource object and
    # here dynamodb is resource name
    client = boto3.resource("dynamodb")

    table = client.Table("login")
    
    if type == "add":
        search = table.query(KeyConditionExpression=Key("email").eq(email))["Items"]
        if search:
            resp = {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                },
                "body": {"Result": "Email already exists"},
            }
        else:
            db_value = table.put_item(
                Item={"email": email, "password": password, "user_name": username}
            )
            resp = {
                "statusCode": 201,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                },
                "body": {"Result": db_value},
            }
    elif type == "options":
        search = table.query(KeyConditionExpression=Key("email").eq(email))["Items"]
        if search:
            resp = {
                "statusCode": 400,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                },
                "body": {"Result": "Email already exists"},
            }
        else:
            db_value = table.put_item(
                Item={"email": email, "password": password, "user_name": username}
            )
            resp = {
                "statusCode": 201,
                "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*",
                },
                "body": {"Result": db_value},
            }
    return resp
