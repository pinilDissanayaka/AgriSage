import os
import json, requests
from dotenv import load_dotenv

load_dotenv('.env')

weatherUrl=os.getenv('WEATHER_API')


complete_url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + '25' + "&q=" + 'colombo'

print(requests.get(complete_url))
