import boto3
from boto3.dynamodb.conditions import Key,Attr
import argparse
import logging
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    email = event["email"]
    artist = event["artist"]
    title = event["title"]
    artist_title = artist + "-" + title
    client = boto3.resource("dynamodb")
    table = client.Table("user_subsongs")
    search = table.query(KeyConditionExpression=Key("email").eq(email) & Key("artist#title").eq(artist_title))["Items"]
    print(search)
    if search:
        resp = {
        "statusCode": 400,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
        },
        "body": {"Result": "User has already subscribed to this song"},
        }
    else:
        queryMS = queryMusic(artist,title)
        for i in queryMS:
            at = i["artist"]
            tt = i["title"]
            img = i["img_url"]
            year = i["year"]
            print(i)
            db_value = table.put_item( Item={"email":email , "artist#title":at + "-" + tt,"artist":at,"title":tt,"img_url":img,"year":year}
            )   
        resp = {
        "statusCode": 201,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
        },
        "body": {"Result": "Successfully subscribed"},
        }
        print(queryMS)
    return resp

def queryMusic (artist,title):
    client = boto3.resource("dynamodb")
    musicTable = client.Table("music")
    response = musicTable.scan(
    FilterExpression=Attr("artist").eq(artist) & Attr("title").eq(title)
    )  
    res = response["Items"]
    for i in res:
        i["img_url"] = generate_presigned_url(i["artist"])
    return res
    
""" REF https://docs.aws.amazon.com/AmazonS3/latest/userguide/example_s3_Scenario_PresignedUrl_section.html"""
def generate_presigned_url(key):
    """
    Generate a presigned Amazon S3 URL that can be used to perform an action.

    :param s3_client: A Boto3 Amazon S3 client.
    :param client_method: The name of the client method that the URL performs.
    :param method_parameters: The parameters of the specified client method.
    :param expires_in: The number of seconds the presigned URL is valid for.
    :return: The presigned URL.
    
    """
    logger = logging.getLogger(__name__)

    s3_client = boto3.client("s3")
    client_method = "get_object"
    method_parameters = {"Bucket": "task2-images", "Key": key + ".jpg"}
    expires_in = 60000
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=client_method, Params=method_parameters, ExpiresIn=expires_in
        )
    except ClientError:
        logger.exception(
            "Couldn't get a presigned URL for client method '%s'.", client_method
        )
        raise
    return url