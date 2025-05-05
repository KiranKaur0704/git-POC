import requests

def get_access_token (eac95919-a7ae-4dad-9b67-43815f6dc5e1, de4ccad4-4712-4ae4-be09-324e43fb8d20, 2acd3806-0d52-4fbc-8f50-b9ffc916859):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')

