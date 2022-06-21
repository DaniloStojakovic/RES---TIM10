import socket
import CollectionDescription
import HistoricalCollection
import WorkerProperty
import LoadBalancerClass
import DataSets
import Code_Names
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
        self.busy= True

        datasetID= DataSets.index(data.dataSet)
        
        for item in data.list:
            wp= WorkerProperty(item.code, item.value)
            self.CD[datasetID].historicalCollection.append(wp)
        
        cd_statuses = []
        
        for cd in self.collection_descriptions:
            code_1, code_2 = False, False
            for wp in cd.historical_collection:
                if wp.code.name == cd.dataset.value[0]:
                    code_1 = True
                elif wp.code.name == cd.dataset.value[1]:
                    code_2 = True
            if code_1 and code_2:
                cd_statuses.append(True)
            else:
                cd_statuses.append(False)

        for cd, ready in zip(self.CD, cd_statuses):
            if ready:
                for wp in cd.historical_collection:
                    if(wp.code == Code_Names.codeNames[1]):
                       print("ovo je za ispis")

       


    def Deadband(old: int, new: int):
        dif = abs(old - new)
        if dif> (old * 0.02):
            return True
        return False