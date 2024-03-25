import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv('.env')

class Migration(object):
    def __init__(self) -> None:
        pass
    
    def connectClient(self):
        try:
            client=MongoClient(os.getenv('MONGO_CLIENT'))
            print("Connected to the mongodb client")
            connectionStatus=True
        except:
            print("Can not connect to the mongodb client")
            connectionStatus=False

        return client, connectionStatus
    
    def migration(self):
        try:
            dbName='AgriSage'
            client, connectionStatus=self.connectClient()
            if connectionStatus:
                db=client[dbName]
                
                userCollection=db['Users']
                user={
                    'name':'test',
                    'phoneNumber':'test',
                    'userName':'test'
                }
                
                    
                
                
        finally:
            client.close()
            
        
    
    