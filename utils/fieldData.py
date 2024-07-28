from mysql import connector
class FieldData(object):
    def connectDB(self, host="localhost", user='root', password="", databaseName="AgriSage"):
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
            sql=f'''
                CREATE TABLE {tableName} (
                    time DATETIME(),
                    temperature FLOAT(5, 5),
                    humidity FLOAT(5, 5),
                    potassium FLOAT(5, 5),
                    nitrogen FLOAT(5, 5),
                    calcium FLOAT(5, 5)
                )
            '''
            
            cursor.execute(sql)
            
        finally:
            cursor.close()
            
            
    def addData(self, tableName:str, data:dict):
        fieldDataDB, cursor=self.connectDB()
        try:
            sql = f''' INSERT INTO {tableName} (name, address) VALUES (%f, %s)'''
            fieldDataDB.commit()
        finally:
            cursor.close()
            
            
            