import requests
from twilio.rest import Client

api_key = "d0121eefffc3fd1330e75875913586c7"

account_sid = 'AC0ea095307309d8f3ab69c3a6a9a975d8'
auth_token = '358a37aa7faf53a0c8761c2019a4e639'

# Rome
MY_LAT = 41.902782
MY_LOT = 12.496365

# # Istanbul
# MY_LAT = 41.008240
# MY_LOT = 28.978359

parameters = {
    "lat": MY_LAT,
    "lon": MY_LOT,
    "appid": api_key,
    "exclude": 'current,minutely,daily'
    # at this step we got rid of the "current,minutely,daily" data so now we can focus on hourly data
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain_today = False

weather_id_codes = []
for code in range(12):
    weather_id = data['hourly'][code]['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain_today = True
    weather_id_codes.append(weather_id)

if will_rain_today:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Don't forget to bring an umbrella!🌧️",
        from_="+13253993865",
        to='+9050X<<<>>>'
    )
    print(message.status)




