import requests
from twilio.rest import Client
from personal import *

parameters = {
    "lat": Lat,
    "lon": Lon,
    "appid": KEY,
    "cnt": 4

}

response = requests.get('https://api.openweathermap.org/data/2.5/''forecast',
                        params=parameters)
response.raise_for_status()

for i in range(4):
    data = response.json()["list"][i]["weather"][0]["id"]
    if data < 700:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_=phone_num1,
            body="It is going to rain today, don't forget your umbrella ☂️",
            to=phone_num2
        )
        break
