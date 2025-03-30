import json

def handler(event, context):
    print("Lambda triggered!")
    return {
        "statusCode": 200,
        "body": json.dumps({ "message": "Hello from Lambda!" })
    }
