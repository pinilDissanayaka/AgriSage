import os
import json, requests
from dotenv import load_dotenv

load_dotenv('.env')

class Weather(object):
    def __init__(self) -> None:
        self._weatherUrl=os.getenv('WEATHER_API')

    def makeUrl(self, location : str):        
        weatherUrl = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + '25' + "&q=" + location
        return weatherUrl
        
    def getWeatherData(self, location:str):
        weatherUrl=self.makeUrl(location=location)
        weatherData=requests.get(self._complete_url)

        return weatherData
