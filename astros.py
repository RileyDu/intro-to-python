import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
# print(json)

print('The people who are currently in space are:')
for person in json['people']:
    print(person['name'])