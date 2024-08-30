from datetime import datetime
from models.fieldData import FieldData
from utils.iotDataDict import IoTDataDict
from database.database import Base, session, engine
import logging

logging.basicConfig(filename="log.log", 
                    level=logging.WARNING)

Base.metadata.create_all(engine)

def addData(data:dict, deviceID:str):
    try:
        newData=FieldData(
            deviceID=deviceID,
            date=datetime.now(),
            potassium=data['potassium'],
            nitrogen=data['nitrogen'],
            phosphorus=data['phosphorus'],
            temperature=data['temperature'],
            humidity=data['humidity'],
            soilMoisture=data['soilMoisture'],
            waterLevel=data['waterLavel'],
            phLavel=data['phLavel']
        )
        session.add(newData)
        session.commit()
        session.refresh(newData)
    except Exception as e:
        logging.exception(e)
        

def getData(deviceID:str):
    try: 
        date=[]
        potassium=[]
        nitrogen=[]
        calcium=[]
        temperature=[]
        humidity=[]
        soilMoisture=[]
        waterLevel=[]
        phLevel=[]
        
        allData=session.query(FieldData).filter_by(deviceID=deviceID).all()
        if allData:
            for data in allData:
                date.append(data.date)
                temperature.append(data.temperature)
                humidity.append(data.humidity)
                potassium.append(data.potassium)
                nitrogen.append(data.nitrogen)
                calcium.append(data.calcium)
                soilMoisture.append(data.soilMoisture)
                waterLevel.append(data.waterLevel)
                phLevel.append(data.phLavel)
                
            iotData=IoTDataDict(date=date, temperature=temperature, humidity=humidity, potassium=potassium, nitrogen=nitrogen, calcium=calcium, soilMoisture=soilMoisture, waterLevel=waterLevel, phLavel=phLevel)
            return iotData     
        else:
            return False
    except Exception as e:
        logging.exception(e)
    
