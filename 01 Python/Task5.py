import requests
from pprint import pprint
import webbrowser

response = requests.get('https://api.ipify.org/?format=json')
x = response.json()
# webbrowser.open('ipinfo.io/'+ x['ip']+'/geo')
urL = f"https://ipinfo.io/{x['ip']}/geo?" 
req = requests.get(urL)
location = req.json()

city = location['city']
region = location['region']
country = location['country']
print('{}{}'.format('city:'.ljust(9), city))
print('{}{}'.format('region:'.ljust(9), region) )
print('{}{}'.format('country:'.ljust(9), country))