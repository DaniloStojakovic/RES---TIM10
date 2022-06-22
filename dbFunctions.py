import sqlite3
from datetime import datetime

class DBFunctions:
    

    def createTable(dataset):
        
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            try:
                cur.execute(f"""create table DATASET_{dataset}(code text not null,
                value int not null,
                date_created timestamp default current_timestamp,
                constraint DATASET_{dataset}_CH check (DATASET_{dataset}.value>=0))""")
            except:
                pass
        

    def GetLastValue (dataset, code):
        
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        
        cur.execute(f"""select value from DATASET_{dataset}
                 where date_created = (select max(date_created) from DATASET_{dataset} where code = '{code}')
            and code = '{code}'""")
        retVal = cur.fetchone()
        print(retVal)
        con.close()
        return retVal
       
   
    

    def Insert(code,value,ds):
        dataset = ds+1
        con = sqlite3.connect('database.db')

        cur = con.cursor()

        
        # Insert a row of data
        cur.execute(f"""insert into DATASET_{dataset} (code, value) values ('{code}', {value})""")

        con.commit()
        con.close() 