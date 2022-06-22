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
            CollectionDescription(0, DataSets.DataSet1, []),
            CollectionDescription(1, DataSets.DataSet2, []),
            CollectionDescription(2, DataSets.DataSet3, []),
            CollectionDescription(3, DataSets.DataSet4, [])
        ]

    def Start(self, data : LoadBalancerClass.LoadBalancerDescriptionCl):
        if self.busy or not self.state:
            return
        self.busy= True
        print("proslo")
        datasetID= DataSets.index(data.dataSet)
        
        for item in data.list:
            wp= WorkerProperty(item.code, item.value)
            self.CD[datasetID].historicalCollection.append(wp)
        
        cd_statuses = []
        
        for cd in self.collection_descriptions:
            code1, code2 = False, False
            for wp in cd.historical_collection:
                if wp.code.name == cd.dataset.value[0]:
                    code1 = True
                if wp.code.name == cd.dataset.value[1]:
                    code2 = True
            if code1 and code2:
                cd_statuses.append(True)
            else:
                cd_statuses.append(False)

        for cd, ready in zip(self.CD, cd_statuses):
            if ready:
                for wp in cd.historical_collection:
                    
                   
                    if(self.Validation(wp)):
                      dbFunctions.DBFunctions.Insert(cd.id, wp.code.name, wp.WorkerValue)
                    else:
                        self.CD[cd.id].historicalCollection.reomve[wp]
        
        self.busy= False   
       



    def Validation(self, wp: WorkerProperty):
        for dataset in range(1, 5):
            dbFunctions.DBFunctions.createTable(dataset)
        if wp.code == Code_Names.CODE_DIGITAL:
            return True
        else:
            dataset = self.getDataSet(wp.code)
            last = dbFunctions.DBFunctions.GetLastValue(dataset, wp.code)
            if not last:
                return True
            return self.Deadband(last, wp.WorkerValue)
        
            

        

    def Deadband(old: int, new: int):
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
lista={aa,bb}
des = LoadBalancerClass.LoadBalancerDescriptionCl(1,lista,1)
chida=Worker(1,True,False)
chida.Start(des)
print("radi")
