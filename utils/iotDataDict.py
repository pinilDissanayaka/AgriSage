from typing import TypedDict
import logging

logging.basicConfig(filename="logging.txt")


class IoTDataDict(TypedDict):
    date=[]
    potassium=[]
    nitrogen=[]
    calcium=[]
    temperature=[]
    humidity=[]
    soilMoisture=[]
    waterLevel=[]
    
    