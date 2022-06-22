import sqlite3
from datetime import datetime

class DBFunctions:
    

    def createTable(self,dataset):
        
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            self.connection.execute(f"""create table DATASET_{dataset}(code text not null,
            value int not null,
            date_created timestamp default current_timestamp,
            constraint DATASET_{dataset}_CH check (DATASET_{dataset}.value>=0))""")
        

    def Exist(self,id,dataset):
        retVal = self.connection.execute(f"""
            SELECT id,code,value,timestamp
            FROM dataset{dataset}
            WHERE id = {id}
            """)
        if(len(retVal.fetchall))>0:
            return True
        return False

   

    def GetLastValue (self, dataset, code):
        con = sqlite3.connect('database.db')
        cur = con.cursor()

        cur.execute(f"""select value from DATASET_{dataset}
            t max(date_created) from DATASET_{dataset} where code = '{code}')
        and code = '{code}'""")
        retVal = cur.fetchone()
        con.close()

        return retVal
        
   
    

    def Insert(self,code,value,dataset):
        con = sqlite3.connect('database.db')

        cur = con.cursor()

        dtime = datetime.now()
        # Insert a row of data
        cur.execute(f"""insert into DATASET_{dataset} (code, value) values ('{code}', {value})""")

        con.commit()
        con.close() 