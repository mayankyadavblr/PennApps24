import arrow
import requests
import json

start = arrow.now().floor('day')

end = arrow.now().ceil('day')

response = requests.get(
  'https://api.stormglass.io/v2/weather/point',
  params={
    'lat': 58.7984,
    'lng': 17.8081,
    'params': ','.join(['humidity']),
    'start': start.to('UTC').timestamp(),  
    'end': end.to('UTC').timestamp()  
  },
  headers={
    'Authorization': '3064933e-4f55-11ee-92e6-0242ac130002-306493b6-4f55-11ee-92e6-0242ac130002'
  }
)

print(json.dumps(response.json(), indent=4))
