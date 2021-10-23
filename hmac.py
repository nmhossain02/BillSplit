import requests
import base64


def login(username, password):
    url = "https://gateway-staging.ncrcloud.com/security/authentication/login"
    decoded = f'{username}:{password}'
    encoded = base64.b64encode(decoded.encode()).decode("ISO-8859-1")

    headers = {
        'Authorization': f'Basic {encoded}'
    }

    response = requests.request("POST", url, headers=headers, data={})
    token = response.json()['token']

    return f'AccessToken {token}'