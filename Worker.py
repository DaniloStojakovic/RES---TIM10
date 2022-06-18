import socket
import CollectionDescription
import HistoricalCollection
import WorkerProperty

class Worker:
    def __init__(self, id, state = false, busy = false ):
       self.id = id
       self.state = state
       self.busy = busy

    
