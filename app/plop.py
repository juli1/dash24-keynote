import requests

def func(arg):
    requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
