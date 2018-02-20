import requests

token = 'd43e382f925bfd9db775fac4f46980ede6f3c6af139fb9e7aa2f850ed0ba12d81f9046a62b1d420da21fe'

first_user = input('First User ')
second_user = input('Second User ')

params = {
    'source_uid': first_user,
    'target_uid': second_user,
    'access_token': token
}

res = requests.get('https://api.vk.com/method/friends.getMutual', params)

print(res.json())
