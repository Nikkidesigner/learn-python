from urllib import request
import requests
from pprint import pprint
import json
url = "http://api.weatherapi.com/v1/current.json?key=8082f4a780034775bf5112531250403&q=London&aqi=no"

r = request.urlopen(url)

data = json.loads(r.read().decode()) 
# pprint(data)
# pprint(data['location']['country'])


r_1 = requests.get(url)
data_1 = r_1.json()
pprint(data_1)