import boto3
import json

cognito = boto3.client('cognito-idp')


def lambda_handler(event, context):
    print(json.dumps(event, indent=2))

    cpf = event['headers']['cpf_cliente']
    password = event['headers']['senha_cliente']
    client_id = '5knk8gad7neb3h7n91rpcigicu'

    try:
        response_cognito = cognito.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': cpf,
                'PASSWORD': password
            },
            ClientId=client_id
        )

        print(json.dumps(response_cognito, indent=2))

        response = generatePolicy(cpf, 'Allow', event['methodArn'], cpf)

    except Exception as error:

        print('Cognito Response ----- : ' + error.__str__())

        response = generatePolicy(cpf, 'Deny', event['methodArn'], cpf)

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
