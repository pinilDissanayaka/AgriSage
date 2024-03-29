import os
import json, requests
from dotenv import load_dotenv
import json

load_dotenv('.env')

class Weather(object):
    def __init__(self) -> None:
        self._weatherAPIKey=os.getenv('WEATHER_API')

    def makeUrl(self, location : str):        
        weatherUrl =f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self._weatherAPIKey}&units=metric"
        return weatherUrl
    
    def makePollutionUrl(self, lat, lon):        
        weatherUrl =f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={self._weatherAPIKey}&units=metric"
        return weatherUrl
        
    def makeForcastUrl(self, lat, lon):
        weatherUrl=f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={self._weatherAPIKey}&units=metric'
        return weatherUrl
        
    def getWeatherData(self, location :str):
        weatherUrl=self.makeUrl(location=location)
        weatherData=requests.get(weatherUrl)
        weatherDataJson=weatherData.json()
        return weatherDataJson
    
    def getweatherForecast(self, lat=6.9, lon=79.8):
        weatherUrl=self.makeForcastUrl(lat=lat, lon=lon)
        weatherForecast=requests.get(weatherUrl)
        weatherForecastJson=weatherForecast.json()
        return weatherForecastJson
        
    def getAirPollutionData(self, lat=6.9, lon=79.8):
        pollutionUrl=self.makePollutionUrl(lat=lat, lon=lon)
        airPollutionData=requests.get(pollutionUrl)
        airPollutionJson=airPollutionData.json()
        return airPollutionJson
        
        
        
        
        

    
        
        
        
        

    

    

