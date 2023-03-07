import urllib.request
import json

APIKEY = '756b1938810423b43e6ac1212d9d40fc'
city = 'Wellesley'
country_code = 'us'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

# print(url)
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
print(response_data)

# How do we get current temperature?
temperature = (response_data['main']['temp']- 273.15) * 9/5 + 32
print(f"{temperature:.2f}")