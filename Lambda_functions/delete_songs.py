import json
import boto3
from boto3.dynamodb.conditions import Key,Attr


def lambda_handler(event, context):
    email = event["email"]
    artist = event["artist"]
    title = event["title"]
    artist_title = artist + "-" + title
    client = boto3.resource("dynamodb")
    table = client.Table("user_subsongs")
    search = table.scan(FilterExpression=Attr("email").eq(email) & Attr("artist").eq(artist) & Attr("title").eq(title))["Items"]
    print(search)
    if len(search) == 0:
        resp = {
        "statusCode": 400,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
        },
        "body": {"Result": "Subscription not found"},
        }
    else:
        db_value = table.delete_item(
         Key={
            'email': email,
            'artist#title': artist_title
            }
        )   
        resp = {
        "statusCode": 201,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
        },
        "body": {"Result": "Successfully deleted"},
        }
    return resp
