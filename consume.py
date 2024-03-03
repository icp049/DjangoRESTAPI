#consume data here


import requests


response = requests.get('http:///drinks/')
print(response.json())