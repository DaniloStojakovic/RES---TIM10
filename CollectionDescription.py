
class WorkerProperty:
     def __init__(self, code, WorkerValue):
            self.code = code
            self.WorkerValue = WorkerValue

WorkerProperties=[]
    
class HistoricalCollection:
     def __init__(self, WorkerProperties):
            self.workerProperties = WorkerProperties

class CollectionDescription:
    def __init__(self, id, DataSets, HistoricalCollection):
            self.id = id
            self.dataSet = DataSets
            self.historicalCollection = HistoricalCollection

 




