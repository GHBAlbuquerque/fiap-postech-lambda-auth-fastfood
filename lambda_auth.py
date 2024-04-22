import boto3
import json

cognito = boto3.client('cognito-idp')
def lambda_handler(event, context):
    print(event)

    username = event['username']
    password = event['password']
#    cpf = event['cpf']

    print(username)
    print(password)

    user_pool_id = 'us-east-1_0ZFQyIZJR'
    client_id = 'cliente1'
    response = cognito.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientId=client_id
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response)
    }
