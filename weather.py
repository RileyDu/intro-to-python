import requests
city = 'Souix Falls'
url = 'http://api.weatherapi.com/v1/current.json?key=b661d7bf48bf43a7857163643240205&q=' + city + '&aqi=no'

response = requests.get(url)

weather_json = response.json()

temp = weather_json.get('current').get('temp_f')

description = weather_json.get('current').get('condition').get('text')

print("Today's weather in", city, " is", temp, "degrees, with", description)