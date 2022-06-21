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
                

                



        while True:
            read_list, write_list, exception_list = select.select(self.sockets, [], [])
            for sock in read_list:
                # new connection
                if sock == self.cs_socket:
                    print ('='*40+'flow start'+'='*39)
                    self.on_accept()
                    break
                # incoming message from a client socket
                else:
                    try:
                        # In Windows, sometimes when a TCP program closes abruptly,
                        # a "Connection reset by peer" exception will be thrown
                        data = sock.recv(4096) # buffer size: 2^n
                        if data:
                            self.on_recv(sock, data)
                        else:
                            self.on_close(sock)
                            break
                    except:
                        sock.on_close(sock)
                        break

    def on_accept(self):
        client_socket, client_addr = self.cs_socket.accept()
        server_ip, server_port = self.select_server(SERVER_POOL, self.algorithm)

        # init a server-side socket
        ss_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            ss_socket.connect((server_ip, server_port))
            #print ('init server-side socket: %s') % (ss_socket.getsockname(),)
            #print ('server connected: %s <==> %s') % (ss_socket.getsockname(),(socket.gethostbyname(server_ip), server_port))
        except:
            print ("Can't establish connection with remote server, err: %s") % sys.exc_info()[0]
            print ("Closing connection with client socket %s") % (client_addr,)
            client_socket.close()
            return

        self.sockets.append(client_socket)
        self.sockets.append(ss_socket)

        self.flow_table[client_socket] = ss_socket
        self.flow_table[ss_socket] = client_socket

    def on_recv(self, sock, data):
        print ('recving packets: %-20s ==> %-20s, data: %s') % (sock.getpeername(), sock.getsockname(), [data])
    

    def on_close(self, sock):
        
        print ('='*41+'flow end'+'='*40)

        ss_socket = self.flow_table[sock]

        self.sockets.remove(sock)
        self.sockets.remove(ss_socket)

        sock.close()  # close connection with client
        ss_socket.close()  # close connection with server

        #del self.flow_table[sock]
        #del self.flow_table[ss_socket]

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