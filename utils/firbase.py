import firebase_admin
from firebase_admin import db, credentials
import os
from dotenv import load_dotenv

load_dotenv(".env")

class Firebase(object):
    def __init__(self) -> None:
        self.cred=credentials.Certificate('agrisage-85205-firebase-adminsdk-6ih1w-881ad47372.json')
        firebase_admin.initialize_app(self.cred, {'databaseURL' : os.getenv('FIREBASE_URL')})
        
    def getValue(self, key:str):
        value=db.reference(key).get()
        return value
        
            

