from multiprocessing.connection import Client
account_sid = os.environ.get("account_sid")#FROM TWILIO WEBSITE
auth_token = environ.get("auth_token") #FROM TWILIO WENSITE
API_KEY = environ.get("API_KEY")  #FROM API WENSITE
# https://api.openweathermap.org/data/2.5/weather?lat=18.520430&lon=73.856743&appid=6abc354a24000b4c1524033a604ca328
import requests
from twilio.rest import Client
import os
weather =\
    {"lat":"18.520430",
    "lon":"73.856743",
    "appid":API_KEY,
    "cnt":4,}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=weather)
response.raise_for_status()
will_rain = False
data = response.json()
for hour_dara in data["list"]:
    condition_code = hour_dara["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    # account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    # auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    # print(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's raining outside  in PUNE☔️",
    #     from_="+********",
    #     to="+91********",
    # )
    message = client.messages.create(
        from_='+16187403743',
        body="It's raining outside 🌧️",
        to='+16187403743'
    )
    # print(message.sid)


