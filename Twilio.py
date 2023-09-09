# Importing required libraries
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily, Monthly
from statistics import mean
import os
from twilio.rest import Client

def collect_weather(lat, long):
    # Set time period
    start = datetime(2022, 1, 1)
    end = datetime(2022, 12, 31)

    # Create Point
    location = Point(lat, long)

    # Get daily data for 2022
    data = Daily(location, start, end)
    data = data.fetch()
    try:
        temp_avg = mean(data["tavg"])
        prcp_avg = sum(data["prcp"])
        return temp_avg, prcp_avg
    except:
        print("No weather data found")
        return None, None

def send_sms(message_body):
    account_sid = 'ACa1724f4ca98de87b1ed387eec79e157d'
    auth_token = 'd3c67ebb320d8d253661546144e0fe0c'
    
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=message_body,
                     from_='+18335095612',
                     to='+16504715598'
                 )
    print(message.sid)

if __name__ == '__main__':
    temperature, precipitation = collect_weather(19.113798345335507, 72.87895812770725)
    
    if temperature and precipitation:
        message_body = f'Average Temperature for today: {temperature:.2f}°C\nTotal Precipitation for today: {precipitation:.2f}mm'
        send_sms(message_body)
    else:
        print("Failed to fetch weather data.")
