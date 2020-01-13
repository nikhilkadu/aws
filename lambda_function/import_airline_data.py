import boto3
import csv
import uuid

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file_name = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(csv_file_name)
    csv_object = s3_client.get_object(Bucket=bucket, Key=csv_file_name)
    csvFileReader = csv.DictReader(csv_object['Body'].read().decode('utf-8').split('\r\n'))

    table = dynamodb.Table('airlines')
    for record in csvFileReader:
        for key in record.keys():
            if not record[key]: record[key] = "None"
        record["id"] = str(uuid.uuid1())
        print(record)
        table.put_item(Item=record)
