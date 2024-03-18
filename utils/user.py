import os
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient
import re
import base64

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
    
    
    
        
    def addUser(self, name:str, phoneNumber:str, userName:str, password:str, adminUserFlag='False'):
        try:
            client, collection, connectionStatus=User.connectDB()
            
            if connectionStatus is True:
                _, user=self.getUserByUserName(userName)
        
                
                if user is None:
                    password=self._bycrypt.generate_password_hash(password).decode('utf-8')
                    
                    collection.insert_one({"name" : name, "phoneNumber" : phoneNumber, "userName" : userName, "password" : password, 'adminUserFlag' : adminUserFlag})
                    print("User successfully added.")
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
        finally:
            client.close()
        return status, user
            
        
    
    def updateUser(self, userName : str, name : str, userNameEdited : str, country : str, address:str, phoneNumber:str, encodedProfilePicture):
        try:
            client, collection, connectionStatus=User.connectDB()
            
            if connectionStatus is True: 
                    collection.update_one({'userName' : userName}, {'$set' : {'name' : name, 'phoneNumber': phoneNumber, 'country' : country, 'address': address, 'phoneNumber': phoneNumber, 'userName' : userNameEdited, 'encodedProfilePicture' : encodedProfilePicture}})   
                    status=True  
            else:
                status=False
               
        finally:
            client.close()
            
        return status
    
    def updateProfilePicture(self, userName : str, profilePicture):
        try:
            client, collection, connectionStatus=User.connectDB()
            
            if connectionStatus is True: 
                encodedProfilePicture=base64.b64encode(profilePicture.read()).decode('utf-8')
                collection.update_one({'userName' : userName}, {'$set' : {'encodedProfilePicture' : encodedProfilePicture}})   
                status=True  
            else:
                status=False
               
        finally:
            client.close()
            
        return status
    
    
    
    def changePassword(self, userName:str, oldPassword:str, newPassword:str):
        try:
            client, collection, connectionStatus=User.connectDB()
            _, user=self.getUserByUserName(userName=userName)
            if user is None:
                status="User not found"
            else:
                isValid =self._bycrypt.check_password_hash(user['password'], oldPassword)
                if isValid:
                    newPassword=self._bycrypt.generate_password_hash(newPassword).decode('utf-8')
                    collection.update_one({'userName' : userName}, {'$set' : {'password' : newPassword}})
                    status='Password change successfully'
                else:
                    status='Can not change password'   
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
        


        


    
        