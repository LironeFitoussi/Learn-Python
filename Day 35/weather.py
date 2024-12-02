import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("API_KEY")
account_sid =  os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

parameters = {
    "lat": 32.338305,
    "lon": 34.856764,
    "appid": api_key,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_forecast = response.json()["list"]

# Loop through the forecast and return a list of weather ids
forecast_ids = [item["weather"][0]["id"] for item in weather_forecast]

# Check if at least one of the weather ids is less than 700
if any(weather_id > 700 for weather_id in forecast_ids):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Bring an umbrella, it is going to rain today',
        to='whatsapp:+972585109829'
    )
    print(message.sid)
else:
    print("No rain today")

    



# print(forcast_tupples)