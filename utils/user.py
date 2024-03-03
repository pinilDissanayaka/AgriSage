import os
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient
import re

load_dotenv(".env")

class User(object):
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
    
    
    
        
    def addUser(self, name:str, phoneNumber:str, userName:str, password:str):
        try:
            client, collection, connectionStatus=User.connectDB()
            
            if connectionStatus is True:
                _, user=self.getUserByUserName(userName)
        
                
                if user is None:
                    password=self._bycrypt.generate_password_hash(password).decode('utf-8')
                    
                    collection.insert_one({"name" : name, "phoneNumber" : phoneNumber, "userName" : userName, "password" : password})
                    print("User successfully added")
                    status=True
                else:
                    print("Failed adding user.")
                    status=False
        finally:
            client.close()
        
        return status
    
          
    def getUserByUserName(self, userName : str):
        try:
            client, collection, connectionStatus=User.connectDB()
            if connectionStatus is True:
                user=collection.find_one({"userName" : userName})
                if user is None:
                    status='User not found'
                else:
                    status='User was found'
                
        finally:
            client.close()
            
        return status, user
    
    
    def logInUser(self, userName:str, password:str):
        try:
            client, collection, connectionStatus=User.connectDB()
        
            if connectionStatus is True:
                _, user=self.getUserByUserName(userName)
            
                if user is None:
                    status="User not found"
                    print("User not found")
                else:
                    isValid =self._bycrypt.check_password_hash(user['password'], password)
                    
                    if isValid:
                        print("Loging successfull")
                        user=user
                        status="Loging successfull"
                    else:
                        print("Incorrect password")
                        user=None
                        status="Incorrect password"
            return status, user
        finally:
            client.close()
            
        
    
    def updateUser(self, userName, username=None, userNameEdited=None, phoneNumber=None, name=None, password=None):
        try:
            client, collection, connectionStatus=User.connectDB()
            
            if connectionStatus is True:     
                if not userNameEdited is None:
                    collection.update_one({'username' : userName}, {'$set' : {'username' : userNameEdited}})
                    status=True
            
                if not phoneNumber is None:
                    collection.update_one({'username' : userName}, {'$set' : {'phoneNumber' : phoneNumber}})
                    status=True
        
                if not name is None:
                    collection.update_one({'username' : userName}, {'$set' : {'name' : name}})   
                    status=True
                    
                if not password is None:
                    password=password=self._bycrypt.generate_password_hash(password).decode('utf-8')
                    collection.update_one({'username' : userName}, {'$set' : {'password' : password}})
                    status=True
                             
            else:
                status=False
               
        finally:
            client.close()
            
        return status
            
    

    def deleteUser(self, userName: str):
        try:
            client, collection, connectionStatus=User.connectDB()
            
            if connectionStatus is True:
                collection.delete_one({"userName" : userName})
                status=True
            else:
                status=False
        finally:
            client.close()
        
        return status
    

    def validatePassword(self, password : str):
        
        status="Valid password"
        
        if len(password) < 6:
            status="Password must contains at least 6 charactors"
        
        if not re.search(r'[a-z]', password):
            status="Password must contains at least one lowercase letter"

        if not re.search(r'[0-9]', password):
            status="Password must contains at least one digit"

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            status="Password must contain at least one special character"
        
        return status
        


        


    
        