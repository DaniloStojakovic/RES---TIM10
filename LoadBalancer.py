import sys
import socket
import select
import random
from itertools import cycle
import pickle
from WriterClass import WriterClass
from Description import Description

SERVER_POOL = [('localhost', 4000), ('localhost', 5000), ('localhost', 6000), ('localhost', 7000)]

ITER = cycle(SERVER_POOL)
def round_robin(iter):
    return next(iter)


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

WorkerSocket = socket.socket()
host2 = 'localhost'
port2 = 6969
WorkerSocket.connect((host2, port2))

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

        ItemList = []
        brojItema = 0

        while True:
            data = client_socket.recv(4096)
            data1 = pickle.loads(data)
            if not data1:
                # if data is not received break
                break
            item = WriterClass(data1.code, data1.value)
            print(f" code:{item.code}  lista vrednost: {item.value}\n")
            if item.code == 'ON' or item.code == 'OFF':
                print('a')
            else:
                brojItema = brojItema + 1
                ItemList.append(item)
                dataset = which_dataset(item.code)
                Desc = Description(brojItema, ItemList, dataset)
                poruka =Desc
                zaSlanje = pickle.dumps(poruka)
                WorkerSocket.send(zaSlanje)
                

    def on_recv(self, sock, data):
        print ('recving packets: %-20s ==> %-20s, data: %s') % (sock.getpeername(), sock.getsockname(), [data])
    

    def select_server(self, server_list, algorithm):
        if algorithm == 'random':
            return random.choice(server_list)
        elif algorithm == 'round robin':
            return round_robin(ITER)
        else:
            raise Exception('unknown algorithm: %s' % algorithm)

if __name__ == '__main__':
    try:
        LoadBalancer('localhost', 5555, 'round robin').start()
    except KeyboardInterrupt:
        print ("Ctrl C - Stopping load_balancer")
        sys.exit(1)