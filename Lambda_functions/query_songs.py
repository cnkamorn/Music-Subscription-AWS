import boto3
from boto3.dynamodb.conditions import Key,Attr
import argparse
import logging
from botocore.exceptions import ClientError


def lambda_handler(event, context):
    client = boto3.resource("dynamodb")
    table = client.Table("music")
    artist = event["artist"]
    title = event["title"]
    year = event["year"]
    if (artist == "" and title == "" and year != ""):
        response = table.scan(
        FilterExpression=Attr("year").eq(year),
        ProjectionExpression = "#yr,artist,title,img_url",
        ExpressionAttributeNames= { "#yr": "year", }
        )  
    elif (artist == "" and title != "" and year == ""):
        response = table.scan(
        FilterExpression=Attr("title").eq(title)
        )  
    elif (artist != "" and title == "" and year == ""):
        response = table.scan(
        FilterExpression=Attr("artist").eq(artist)
        )  
    elif (artist != "" and title != "" and year == ""):
         response = table.scan(
        FilterExpression=Attr("artist").eq(artist) & Attr("title").eq(title)
        )  
    elif (artist != "" and title == "" and year != ""):
        response = table.scan(
        FilterExpression=Attr("year").eq(year) & Attr("artist").eq(artist),
        ProjectionExpression = "#yr,artist,title,img_url",
        ExpressionAttributeNames= { "#yr": "year", }
        )
    elif (artist == "" and title != "" and year != "" ):
        response = table.scan(
        FilterExpression=Attr("year").eq(year) & Attr("title").eq(title),
        ProjectionExpression = "#yr,artist,title,img_url",
        ExpressionAttributeNames= { "#yr": "year", }
        )
    else:
        response = table.scan(
        FilterExpression=Attr("artist").eq(artist) & Attr("title").eq(title) & Attr("year").eq(year),
        ProjectionExpression = "#yr,artist,title,img_url",
        ExpressionAttributeNames= { "#yr": "year", }
        )  
    response = response["Items"]
    for i in response:
        i["img_url"] = generate_presigned_url(i["artist"])
    return response

    
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
        logger.info("Got presigned URL: %s", url)
    except ClientError:
        logger.exception(
            "Couldn't get a presigned URL for client method '%s'.", client_method
        )
        raise
    return url