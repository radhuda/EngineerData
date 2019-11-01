import json
import boto3
import gzip
from io import BytesIO


def lambda_handler(event, context):
    bucket = event["Records"][0]['s3']['bucket']['name']
    key = event["Records"][0]['s3']['object']['key']
    s3 = boto3.client('s3')
    new_key = key[:-3]

    s3.upload_fileobj(
        Fileobj=gzip.GzipFile(
            None,
            'rb',
            fileobj=BytesIO(
                s3.get_object(Bucket=bucket, Key=key)['Body'].read())),
        Bucket=bucket,
        Key=new_key)

    s3r = boto3.resource("s3")
    s3r.Object(bucket, key).delete()