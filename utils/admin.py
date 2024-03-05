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
    def connectDB(cls, databaseName = 'AgriSage', collectionName='Users'):
        try:
            client=MongoClient(os.getenv('MONGO_CLIENT'))
            db=client[databaseName]
            collection=db[collectionName]
            connectionStatus=True
        except:
            print("Database connection failed!")
            connectionStatus=False

        return client, collection, connectionStatus
    

    
          
    def getAdminByUserName(self, userName : str):
        try:
            client, collection, connectionStatus=self.connectDB()
            if connectionStatus is True:
                user=collection.find_one({"userName" : userName})
                if user is None:
                    status='Admin not found'
                else:
                    status='Admin was found'
                
        finally:
            client.close()
            
        return status, user
    
    
    def logInAdmin(self, userName:str, password:str):
        try:
            client, collection, connectionStatus=self.connectDB()
        
            if connectionStatus is True:
                _, user=self.getAdminByUserName(userName)
            
                if user is None:
                    status="Admin not found"
                    print("Adim not found")
                else:
                    isValid =self._bycrypt.check_password_hash(user['password'], password)
                    
                    if isValid:
                        print("Admin Loging successfull")
                        user=user
                        status="Admin Loging successfull"
                    else:
                        print("Incorrect password")
                        user=None
                        status="Incorrect password"
        finally:
            client.close()
        return status, user
            
        
    
    
    