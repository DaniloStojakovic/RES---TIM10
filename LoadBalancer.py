from multiprocessing import Process
import socket
import pickle
import threading
from WriterClass import WriterClass
from Description import Description
from Worker import Worker
import Logger

def which_dataset(code):
        if code == "CODE_ANALOG" or code == "CODE_DIGITAL":
            dataset = 1
        if code == "CODE_CUSTOM" or code == "CODE_LIMITSET":
            dataset = 2
        if code == "CODE_SINGLENOE" or code == "CODE_MULTIPLENODE":
            dataset = 3
        if code == "CODE_CONSUMER" or code == "CODE_SOURCE":
            dataset = 4
        return dataset

WorkerList1 = []
WorkerList2 = []

class LoadBalancer(object):

    flow_table = dict()
    sockets = list()

    def __init__(self, ip, port, algorithm='round robin'):
        self.ip = ip
        self.port = port
        self.algorithm = algorithm
        self.cs_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cs_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.cs_socket.bind((self.ip, self.port))
        self.cs_socket.listen(1)
        self.sockets.append(self.cs_socket)

    def start(self):
        client_socket, client_addr = self.cs_socket.accept()
        print ('='*40+'flow start'+'='*39)
        print('Client connected: %s', client_addr)

        ItemList1 = []
        ItemList2 = []
        ItemList3 = []
        ItemList4 = []
        brojItema = 2
        brojacWorkera = 1
        descID = 1
        dataset = which_dataset('CODE_ANALOG')
        Desc1 = Description(brojItema, ItemList1, 1)
        Desc2 = Description(brojItema, ItemList2, 2)
        Desc3 = Description(brojItema, ItemList3, 3)
        Desc4 = Description(brojItema, ItemList4, 4)

        while True:
            data = client_socket.recv(4096)
            data1 = pickle.loads(data)
            if not data1:
                # if data is not received break
                continue
            item = WriterClass(data1.code, data1.value)
            print(f"Provera. Load Balancer primio od Workera kod: {data1.code} i vrednost: {data1.value}\n")
            Logger.logger.info("Load Balancer: Upisan novi podatak u load balanceru")
            if item.code == 'ON':
                if item.value in WorkerList1:
                    print('Worker je vec ukljucen\n')
                    Logger.logger.info("Load Balancer: Worker je ukljucen u Load Balanceru")
                    continue
                else:
                    print('WORKER UPALJEN\n')
                    worker = Worker(brojacWorkera, True, False)
                    brojacWorkera = brojacWorkera + 1
                    if descID ==1:
                        Worker1 = Process(target=Worker.Start, args=(worker,Desc1))
                        descID = descID + 1
                    elif descID ==2:
                        
                        Worker1 = Process(target=Worker.Start, args=(worker,Desc2))
                        descID = descID + 1
                    elif descID ==3:
                        Worker1 = Process(target=Worker.Start, args=(worker,Desc3))
                        descID = descID + 1
                    elif descID ==4:
                        Worker1 = Process(target=Worker.Start, args=(worker,Desc4))
                        descID = 1
                    Worker1.start()
                    WorkerList1.append(item.value)
                
            elif item.code == 'OFF':
                print("WORKER UGASEN\n")
                Logger.logger.info("Load Balancer: Worker je iskljucen u Load Balanceru")
            else:
                brojItema = brojItema + 1
                dataset = which_dataset(item.code)
                if dataset == 1:
                    Desc1.listaItema.append(item)
                elif dataset == 2:
                    Desc2.listaItema.append(item)
                elif dataset == 3:
                    Desc3.listaItema.append(item)
                elif dataset == 4:
                    Desc4.listaItema.append(item)
                    

if __name__ == "__main__":  # ovo ispod se nece pozvati pri importovanju
    loadbalancer = LoadBalancer('localhost', 5555, 'round robin')
    startProces = threading.Thread(target=loadbalancer.start)

    startProces.start()