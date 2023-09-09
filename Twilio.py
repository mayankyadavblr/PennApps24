# Importing required libraries
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Monthly
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
    data = Monthly(location, start, end)
    data = data.fetch()
    try:
        temp_avg = mean(data["tavg"])
        prcp_avg = sum(data["prcp"])
        return temp_avg, prcp_avg
    except:
        print("No weather data found")
        return None, None

def send_sms(message_body):
    account_sid = os.environ['ACa1724f4ca98de87b1ed387eec79e157d']
    auth_token = os.environ['[AuthToken]']
    
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body=message_body,
                     from_='YOUR-TWILI0-NUMBER',
                     to='+18149549696'
                 )
    print(message.sid)

if __name__ == '__main__':
    temperature, precipitation = collect_weather(19.113798345335507, 72.87895812770725)
    
    if temperature and precipitation:
        message_body = f'Average Temperature for 2022: {temperature:.2f}°C\nTotal Precipitation for 2022: {precipitation:.2f}mm'
        send_sms(message_body)
    else:
        print("Failed to fetch weather data.")
