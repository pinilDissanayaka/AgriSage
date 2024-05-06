import os
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient
import re

load_dotenv(".env")

class Admin(object):
    def __init__(self, app) -> None:
        self._bycrypt=Bcrypt(app=app)
        
        
    @classmethod
    def connectDB(cls, databaseName = 'AgriSage'):
        try:
            client=MongoClient(os.getenv('MONGO_CLIENT'))
            db=client[databaseName]
            connectionStatus=True
        except:
            print("Database connection failed!")
            connectionStatus=False

        return client, db, connectionStatus
    
    def getDocumentCount(self, collectionName :str, adminUserFlag = None):
        try:
            client, db, connectionStatus=self.connectDB()
            collection=db[collectionName]
            
            if connectionStatus:
                if adminUserFlag is None:
                    count=collection.count_documents({})
                else:
                    count=collection.count_documents({"adminUserFlag" : adminUserFlag})
            else:
                count=None
        finally:
            client.close()
            
        return count
    
    
    
    
        
        
    


            
        
    
    
    