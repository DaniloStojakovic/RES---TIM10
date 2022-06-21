import sqlite3
from datetime import datetime

class DBFunctions:

   
    def dbConnect(self,dataset):
        try:
            self.connection = sqlite3.connect("database.db")
        except:
            return False
        return True

    def createTable(self,dataset):
        try:
            self.connection.execute(f"""
                CREATE TABLE dataset{dataset}
                (
                    id INT PRIMARY KEY NOT NULL,
                    code TEXT NOT NULL,
                    value INT NOT NULL,
                    timestamp TEXT NOT NULL
                )
                """)
        except:
            pass

    def Exist(self,id,dataset):
        retVal = self.connection.execute(f"""
            SELECT id,code,value,timestamp
            FROM dataset{dataset}
            WHERE id = {id}
            """)
        if(len(retVal.fetchall))>0:
            return True
        return False

    def update(self,id,code,value,dataset):
        timestamp = datetime.now()
        self.connection.execute(f"""
            UPDATE dataset{dataset}
            SET code = "{code}", value = {value}, timestamp = "{timestamp}"
            WHERE id = {id}
            """)
        self.connection.commit()

    def getValue(self,id,dataset):
        retVal = self.connection.execute(f"""
            SELECT value
            FROM dataset{dataset}
            WHERE id = {id}
            """)
        value,=retVal.fetchall()[0]
        return value

    def getWithCode(self,code,dataset):
        retVal = self.connection.execute(f"""
            SELECT *
            FROM dataset{dataset}
            WHERE code = {code}
            """)
        return retVal.fetchall()

    def getWithTimestamp(self,firstTimestamp,secondTimestamp,dataset):
        retVal = self.connection.execute(f"""
            SELECT *
            FROM dataset{dataset}
            WHERE timestamp BETWEEN '{firstTimestamp}' AND '{secondTImestamp}'
            """)
        return retVal.fetchall()
               
    def Deadband(self,oldValue,newValue):
        deadband = abs(newValue-oldValue)/ oldValue * 100
        return deadband

    def Insert(self,id,code,value,dataset):
        timestamp = datetime.now()
        self.connection.execute(f"""
            INSERT INTO dataset{dataset} (id,code,value,timestamp)
            VALUES ({id},'{code}',{value},'{timestamp}')
            """)
        self.connection.commit()