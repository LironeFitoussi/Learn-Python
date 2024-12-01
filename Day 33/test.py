import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response)
# print(response.status_code)

# Error handling with raise_for_status()
response.raise_for_status()

# Get the content of the response
data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

# print(f'Longitude: {longitude}')
# print(f'Latitude: {latitude}')

iss_position = (longitude, latitude)
print(iss_position)