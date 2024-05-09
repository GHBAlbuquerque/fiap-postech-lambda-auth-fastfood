import boto3
import json

cognito = boto3.client('cognito-idp')


def lambda_handler(event, context):
    print(event)

    cpf = event['headers']['cpf_cliente']
    password = event['headers']['senha_cliente']
    user_pool_id = 'us-east-1_tDatRvOzb'
    client_id = 'cliente1'

    response = cognito.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': cpf,
            'PASSWORD': password
        },
        ClientId=client_id
    )

    print(response)

    return json.loads(response)


def generatePolicy(principalid, effect, resource, cpf):
    authResponse = {}
    authResponse['principalId'] = principalid
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

# def lambda_handler(event, context):
#     print(event)
#
#     cpf = event['headers']['cpf_cliente']
#     print(cpf)
#
#     if (cpf == "123"):
#         response = generatePolicy(cpf, 'Allow', event['methodArn'], cpf)
#     else:
#         response = generatePolicy(cpf, 'Deny', event['methodArn'], cpf)
#     try:
#         return json.loads(response)
#     except BaseException:
#         print('unauthorized')
#         return 'unauthorized'  # Return a 500 error
