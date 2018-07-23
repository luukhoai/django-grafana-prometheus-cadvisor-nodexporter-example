import requests

for i in range(1000):
    response = requests.get('http://localhost', timeout=1.0)

print('pass')