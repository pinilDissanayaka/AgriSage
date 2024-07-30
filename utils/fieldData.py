from mysql import connector
from datetime import datetime
class FieldData(object):
    def __init__(self, host="localhost", user="root", password="", databaseName="AgriSage") -> None:
        try:
            fieldDataDB=connector.connect(
                host=host,
                user=user,
                password=password
            )
            
            cursor=fieldDataDB.cursor()
            
            sql=f'''
                CREATE DATABASE IF NOT EXISTS {databaseName}
            '''
            
            cursor.execute(sql)
        finally:
            cursor.close()
        
    
    def connectDB(self, host="localhost", user="root", password="", databaseName="AgriSage"):
        try:
            fieldDataDB=connector.connect(
                host=host,
                user=user,
                password=password,
                database=databaseName
            )
            
            cursor=fieldDataDB.cursor()
        except:
            print("Couldn't connect MySQL database.")
            
        return fieldDataDB, cursor

    
    def createFieldDataTable(self, tableName:str):
        _, cursor=self.connectDB()
        try:
            tableName="table_".join(tableName)
            
            sql=f'''
                CREATE TABLE {tableName} (
                    time DATETIME,
                    temperature VARCHAR(10),
                    humidity VARCHAR(10),
                    potassium VARCHAR(10),
                    nitrogen VARCHAR(10),
                    calcium VARCHAR(10)
                )
            '''
            
            cursor.execute(sql)
            
        finally:
            cursor.close()
            
    def deleteFieldDataTable(self, tableName:str):
        _, cursor=self.connectDB()
        try:
            tableName="table_".join(tableName)
            sql=f'''
            DROP TABLE {tableName}
            '''
            cursor.execute(sql)
        finally:
            cursor.close()

            
            
    def addData(self, tableName:str, data:dict):
        fieldDataDB, cursor=self.connectDB()
        try:
            tableName="table_".join(tableName)
            time=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            sql = f''' INSERT INTO {tableName} (time, temperature, humidity, potassium, nitrogen, calcium) 
            VALUES (%s, %s, %s, %s, %s, %s)'''
            values=(
                time,
                str(data['temperature']),
                str(data['humidity']),
                str(data['potassium']),
                str(data['nitrogen']),
                str(data['calcium'])
            )
            
            cursor.execute(sql, values)
            
            fieldDataDB.commit()
        finally:
            cursor.close()
            
            
    def getFieldData(self, tableName:str):
        fieldDataDB, cursor=self.connectDB()
        date=[]
        potassium=[]
        nitrogen=[]
        calcium=[]
        try:
            tableName="table_".join(tableName)
            sql=f'''
                SELECT * FROM {tableName}
            '''
            cursor.execute(sql)
            rows=cursor.fetchall()
            
            for row in rows:
                date.append(row[0])
                potassium.append(row[3])
                nitrogen.append(row[4])
                calcium.append(row[5])
                
        finally:
            cursor.close()
            
        return date, potassium, nitrogen, calcium
            
            