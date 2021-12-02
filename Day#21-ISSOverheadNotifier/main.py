import requests
from datetime import datetime
import smtplib
import time

# istanbul's latitude and longitude
MY_LAT = 41.015137
MY_LOT = 28.979530

MY_EMAIL = "XXXXX"
MY_PASSWORD = "XXXX"
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# """
# An endpoint is one end of a communication channel.
# When an API interacts with another system, the touchpoints of this communication are considered endpoints.
# For APIs, an endpoint can include a URL of a server or service.
# Each endpoint is the location from which APIs can access the resources they need to carry out their function.
# """
# print(response)
# # <Response [200]>
# print(response.status_code)
# # 200
#
# response.raise_for_status()
# # if we don't get 200 for status code it'll catch the exceptions so we do not have to create if else struct to catch errors :)
# """
# RESPONSE CODE MEANINGS :)
# 1XX : Hold on
# 2XX : Here you go - success
# 3XX : Go away - redirection
# 4XX : You screwed up - client error
# 5XX : Server error
# """
# print(response.json())
# # {'timestamp': 1637679177, 'message': 'success', 'iss_position': {'longitude': '152.2763', 'latitude': '19.2658'}}
#
# data =  response.json()
#
# longitude = data['iss_position']['longitude']
# print(longitude)
def iss_overhead():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LOT,
        "formatted": 0
        # "formatted" is an optional parameter

    }
    # if we do not use the required parameters such as lat and lng we get 4xx status code
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_lng = float(data['iss_position']['longitude'])

    if (MY_LAT - 5) <= iss_lat <= (MY_LAT + 5) and (MY_LOT - 5) <= iss_lng <= (MY_LOT + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LOT,
        "formatted": 0
        # "formatted" is an optional parameter
    }
    # if we do not use the required parameters such as lat and lng we get 4xx status code
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[1])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[1])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="The ISS is above you in the sky"
        )
