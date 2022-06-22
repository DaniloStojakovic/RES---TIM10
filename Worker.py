from os import truncate
import socket
import CollectionDescription
import HistoricalCollection
import WorkerProperty 
import LoadBalancerClass
import DataSets
import Code_Names
import dbFunctions

print("radi")

class Worker:
    def __init__(self, id, state = False, busy = False ):
       self.id = id
       self.state = state
       self.busy = busy
       self.CD = [
            CollectionDescription.CollectionDescription(0, DataSets.DataSet1, []),
            CollectionDescription.CollectionDescription(1, DataSets.DataSet2, []),
            CollectionDescription.CollectionDescription(2, DataSets.DataSet3, []),
            CollectionDescription.CollectionDescription(3, DataSets.DataSet4, [])
        ]

    def Start(self, data : LoadBalancerClass.LoadBalancerDescriptionCl):
        if self.busy or not self.state:
            return
        self.busy= True
        print("proslo")
        datasetID = data.dataSet-1
        print(datasetID)
        for item in data.list:
            wp= WorkerProperty.WorkerProperty(item.code, item.value)
            print(item.code)
            print(item.value)
            self.CD[datasetID].historicalCollection.append(wp)
        
        cd_statuses = []
        
        for cd in self.CD:
            code1, code2 = False, False
            for wp in cd.historicalCollection:
                if wp.code == cd.dataSet[0]:
                    code1 = True
                if wp.code == cd.dataSet[1]:
                    code2 = True
            if code1 and code2:
                cd_statuses.append(True)
            else:
                cd_statuses.append(False)

            
        for cd, ready in zip(self.CD, cd_statuses):
            if ready:
                for wp in cd.historicalCollection:
                    if(self.Validation(wp)):
                      dbFunctions.DBFunctions.Insert(wp.code, wp.WorkerValue, cd.id)
                      print("treba da upise")
                    else:
                        self.CD[cd.id].historicalCollection.remove(wp)
        
        self.busy= False   
       



    def Validation(self, wp: WorkerProperty):
        for dataset in range(1, 5):
            dbFunctions.DBFunctions.createTable(dataset)
        if wp.code ==  Code_Names.codeNames[1]:
            return True
        else:
            dataset = self.GetDataSet(wp.code)
            last = dbFunctions.DBFunctions.GetLastValue(dataset, wp.code)
            if not last:
                return True
            last=last[0]
            return self.Deadband(last, wp.WorkerValue)
        
            

        

    def Deadband(self, old: int, new: int):
        dif = abs(old - new)
        if dif> (old * 0.02):
            return True
        return False

    def GetDataSet(self, code ):
        if code == "CODE_ANALOG" or code == "CODE_DIGITAL" :
            return 1
        elif code == "CODE_CUSTOM" or code == "CODE_LIMITSET" :
            return 2
        elif code ==  "CODE_SINGLENOE" or code =="CODE_MULTIPLENODE" :
            return 3
        elif code == "CODE_CONSUMER" or code == "CODE_SOURCE" :
            return 4
      
aa = LoadBalancerClass.LoadBalancerItemCl("CODE_ANALOG",2)
bb = LoadBalancerClass.LoadBalancerItemCl( "CODE_DIGITAL",5)
lista=[]
lista.append(aa)
lista.append(bb)
des = LoadBalancerClass.LoadBalancerDescriptionCl(1, lista, 1)
chida=Worker(1,True,False)
chida.Start(des)
print("radi")
