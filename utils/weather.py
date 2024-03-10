import os
import json, requests
from dotenv import load_dotenv
import json

load_dotenv('.env')

class Weather(object):
    def __init__(self) -> None:
        self._weatherAPIKey=os.getenv('WEATHER_API')

    def makeUrl(self, location : str):        
        weatherUrl = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self._weatherAPIKey}&units=metric"
        return weatherUrl
        
    def getWeatherData(self, location:str):
        self._weatherUrl=self.makeUrl(location=location)
        weatherData=requests.get(self._weatherUrl)
        weatherDataJson=weatherData.json()

        return weatherDataJson
    
    
if __name__=='__main__':
    w=Weather()
    print(w.getWeatherData('colombo'))
