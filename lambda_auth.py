import boto3
import json

cognito = boto3.client('cognito-idp')


def lambda_handler(event, context):
    print(event)

    cpf = event['headers']['cpf_cliente']
    print(cpf)

    if (cpf == "123"):
        response = generatePolicy(cpf, 'Allow', event['methodArn'], cpf)
    else:
        response = generatePolicy(cpf, 'Deny', event['methodArn'], cpf)


def generatePolicy(principalId, effect, resource, cpf):
    authResponse = {}
    authResponse['principalId'] = principalId
    if (effect and resource):
        policyDocument = {}
        policyDocument['Version'] = '2012-10-17'
        policyDocument['Statement'] = []
        statementOne = {}
        statementOne['Action'] = 'execute-api:Invoke'
        statementOne['Effect'] = effect
        statementOne['Resource'] = resource
        policyDocument['Statement'] = [statementOne]
        authResponse['policyDocument'] = policyDocument

    authResponse['context'] = {
        "cpf_cliente": cpf
    }

    authResponse_JSON = json.dumps(authResponse)

    return authResponse_JSON

#     username = event['username']
#     password = event['password']
# #    cpf = event['cpf']
#
#     print(username)
#     print(password)
#
#     user_pool_id = 'us-east-1_tDatRvOzb'
#     client_id = 'cliente1'
#     response = cognito.initiate_auth(
#         AuthFlow='USER_PASSWORD_AUTH',
#         AuthParameters={
#             'USERNAME': username,
#             'PASSWORD': password
#         },
#         ClientId=client_id
#     )
#
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Access-Control-Allow-Origin': '*'
#         },
#         'body': json.dumps(response)
#     }
