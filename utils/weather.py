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
    
    def geocoding(self, location):
        
        geocordingUrl=f'http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={self._weatherAPIKey}'
        geocordingData=requests.get(geocordingUrl)
        geocordingJson=geocordingData.json()
        lat=geocordingJson[0]['lat']
        lon=geocordingJson[0]['lon']
        return lat, lon
        
    def getWeatherData(self, location :str):
        weatherUrl=self.makeUrl(location=location)
        weatherData=requests.get(weatherUrl)
        weatherDataJson=weatherData.json()
        return weatherDataJson
    
    def getweatherForecast(self, location:str):
        lat, lon=self.geocoding(location=location)
        weatherUrl=self.makeForcastUrl(lat=lat, lon=lon)
        weatherForecast=requests.get(weatherUrl)
        weatherForecastJson=weatherForecast.json()
        return weatherForecastJson
        
    def getAirPollutionData(self, location:str):
        lat, lon=self.geocoding(location=location)
        pollutionUrl=self.makePollutionUrl(lat=lat, lon=lon)
        airPollutionData=requests.get(pollutionUrl)
        airPollutionJson=airPollutionData.json()
        return airPollutionJson
        
        
        
        
        

    
        
        
        
        

    

    

