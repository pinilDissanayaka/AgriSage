import firebase_admin
from firebase_admin import db, credentials
import os
from dotenv import load_dotenv
from utils.fieldData import FieldData


load_dotenv(".env")

fieldData=FieldData()

class Firebase(object):
    def __init__(self) -> None:
        self.cred=credentials.Certificate('agrisage-85205-firebase-adminsdk-6ih1w-881ad47372.json')
        firebase_admin.initialize_app(self.cred, {'databaseURL' : os.getenv('FIREBASE_URL')})
        
    def getKeys(self, key:str):
        try:
            keys=db.reference('/').get()
            keys=keys.keys()
        
            if key in keys:
                ifExists=True
            else:
                ifExists=False
            return ifExists
        except:
            return None
    
    def getValue(self, key:str):
        try:
            ifExists=self.getKeys(key=key)
            if ifExists:
                value=db.reference(key).get()
                fieldData.addData(tableName=key, data=value)
                date, potassium, nitrogen, calcium=fieldData.getFieldData(tableName=key)
                value['date']=date
                value['nitrogen']=nitrogen
                value['potassium']=potassium
                value['calcium']=calcium
                print(value)
            else:
                value=False
            return value
        except:
            return None
        

        
    
        
        
            

