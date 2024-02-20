import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table_name=os.environ['DB_NAME']
table = dynamodb.Table(table_name) 

def lambda_handler(event, context):
    operation = event['operation']
    
    if operation == 'insert':
        return insert_record(event)
    elif operation == 'update':
        return update_record(event)
    elif operation == 'delete':
        return delete_record(event)
    elif operation == 'fetch':
        return fetch_records(event)
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid operation'})
        }

def insert_record(event):
    try:
        name = event['name']
        email = event['email']
        attendance = event['attendance']
        date = event['date']
        
        # Generate unique UID
        uid = str(uuid.uuid4())
        
        # Insert record into DynamoDB
        table.put_item(
            Item={
                'uid': uid,
                'name': name,
                'email': email,
                'attendance': attendance,
                'date': date
            }
        )
        
        return {
            'statusCode': 200,
            'body': {
                'response': {'uid': uid}
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {'error': str(e)}
        }

def update_record(event):
    try:
        uid = event['uid']
        attendance = event['attendance']
        
        # Update record in DynamoDB
        table.update_item(
            Key={'uid': uid},
            UpdateExpression='SET attendance = :val',
            ExpressionAttributeValues={':val': attendance}
        )
        
        return {
            'statusCode': 200,
            'body': {
                'response': {'uid': uid}
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {'error': str(e)}
        }

def delete_record(event):
    try:
        uid = event['uid']
        
        # Delete record from DynamoDB
        table.delete_item(
            Key={'uid': uid}
        )
        
        return {
            'statusCode': 200,
            'body': {
                'response': {'uid': uid}
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {'error': str(e)}
        }
        
def fetch_records(event):
    try:
        # Scan DynamoDB table to fetch all records
        response = table.scan()
        items = response['Items']
        
        return {
            'statusCode': 200,
            'body': {
                'records': items
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {'error': str(e)}
        }

# Note Make sure to set up all the ENV variables as well as the lambda function before testing