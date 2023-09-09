import arrow
import requests
import json

start = arrow.get('2021-05-15')
end = arrow.get('2023-05-15')

response = requests.get(
  'https://api.stormglass.io/v2/bio/point',
  params={
    'lat': 58.7984,
    'lng': 17.8081,
    'params': ','.join(['iron', 'nitrate','soilMoisture', 'soilTemperature']),
    'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    'end': end.to('UTC').timestamp(),      # Convert to UTC timestamp
  },
  headers={
    'Authorization': '2d246e16-4ebe-11ee-92e6-0242ac130002-2d246e84-4ebe-11ee-92e6-0242ac130002'
  }
)

print(json.dumps(response.json(), indent=4))
