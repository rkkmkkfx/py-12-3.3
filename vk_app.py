import requests
from urllib.parse import urlencode

APP_ID = 6380141
AUTHORIZE_URL = 'https://oauth.vk.com/authorize'

auth_params = {
    'client_id': APP_ID,
    'redirect_url': 'https://oauth.vk.com/blank.html',
    'display': 'popup',
    'scope': 'friends',
    'response_type': 'token'
}

print('?'.join((AUTHORIZE_URL, urlencode(auth_params))))

token = '7589c9f1f059c7b33efb70a74210aff77688221c65c2310d27afd511a7d6659b26179cbdb36c6ffe9de25'

FIRST_ID = 1
SECOND_ID = 2

def get_mutual(first_user, second_user):
    params = {
        'source_uid': first_user,
        'target_uid': second_user,
        'access_token': token,
        'v': '5.73'
    }

    return requests.get('https://api.vk.com/method/friends.getMutual', params).json()['response']


for user in get_mutual(FIRST_ID, SECOND_ID):
    print('https://vk.com/id{}'.format(user))
