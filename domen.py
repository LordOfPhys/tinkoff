import requests

response = requests.get('https://www.reg.ru/domain/new/')

print(response.content)
