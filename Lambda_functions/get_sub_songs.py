import json
import boto3
from boto3.dynamodb.conditions import Key,Attr

def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("user_subsongs")
    user = event["useremail"]
    response = table.scan(FilterExpression=Attr("email").eq(user))
    return response["Items"]