import os
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from pymongo import MongoClient
import re
import base64
import logging

load_dotenv(".env")
logging.basicConfig(filename='logging')


class Product(object):
    def __init__(self) -> None:
        pass
               
    @classmethod
    def connectDB(cls, databaseName = 'AgriSage', collectionName='Products'):
        try:
            client=MongoClient(os.getenv('MONGO_CLIENT'))
            db=client[databaseName]
            collection=db[collectionName]
            logging.info('Connected to the database')
            connectionStatus=True
        except Exception as e:
            logging.error(e)
            connectionStatus=False
            
        return client, collection, connectionStatus
    
    
    
        
    def addProduct(self, fertilizerName:str, nutrientComposition:str, fertilizerType:str, manufacturer:str):
        try:
            client, collection, connectionStatus=Product.connectDB()
            
            if connectionStatus:                
                collection.insert_one({"fertilizerName" : fertilizerName, "nutrientComposition" : nutrientComposition, "fertilizerType" : fertilizerType, "manufacturer" : manufacturer})
                print("Product successfully added.")
                status=True
            else:
                print("Failed adding product.")
                status=False
        except Exception as e:
            logging.error(e)
        finally:
            client.close()
            
        return status
    
    def updateProduct(self):
        try:
            client, collection, connectionStatus=Product.connectDB()
        finally:
            client.close()
            
    def showAllProducts(self):
        try:
            client, collection, connectionStatus=Product.connectDB()
            if connectionStatus:
                products=collection.find()
                if products:
                    return products
                else:
                    products=None
                    return products
            else:
                products=None
                return products
        except Exception as e:
            logging.error(e)
        finally:
            client.close()
            