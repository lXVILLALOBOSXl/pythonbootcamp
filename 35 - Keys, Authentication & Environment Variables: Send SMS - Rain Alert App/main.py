import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = 20.671955
MY_LONG =-103.416504


account_sid = "AC3472ee9a96d72588b2f82772eb5606ca"
auth_token = os.environ.get("TWILIO_API_KEY")


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": 4
}

try:
    reponse = requests.get(OWM_ENDPOINT, params=parameters)
    reponse.raise_for_status()
    weather_data = reponse.json()

    for item in weather_data["list"]:
        if item["weather"][0]["id"] < 700:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='+12706068224',
                body="It's going to rain today. Remember to bring an Umbrella ☔️",
                to=''
            )
            print(message.status)
            break
except:
    print(f"Error has occured")
