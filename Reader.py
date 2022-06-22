#reader
import Logger
import dbFunctions
import DataSets
import Code_Names
import CollectionDescription
import HistoricalCollection
import pickle
import socket
import sys

sys.path.append('../')

from _thread import start_new_thread

workerAddress = 'localhost'
workerPort = 55000
workerHost = (workerAddress, workerPort)

readerAddress = 'localhost'
readerPort = 33000
readerHost = (readerAddress, readerPort)

def getFromWorker(string):
    workerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"connecting to Worker on [ADDR:PORT] : [{str(workerAddress)}:{str(workerPort)}]")
    Logger.logger.info(f"connecting to Worker on [ADDR:PORT] : [{str(workerAddress)}:{str(workerPort)}]")
    workerSocket.connect(workerHost)

    try:
        workerSocket.send(pickle.dumps(string.encode("utf-8")))
        reply = workerSocket.recv(1024)
        workerSocket.close()
        print(reply.decode("utf-8"))
        Logger.logger.info(reply.decode("utf-8"))
        return reply

    except Exception as e:
        workerSocket.close()
        print(e)
        Logger.logger.error(e)
        return "ERROR"



def getParameters(data):
    option = data.split(',')[0]
    parameter = data.split(',')[1]
    parameter = parameter[1:]
    return option,parameter

def multiThreadedConnection(connection): 
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            data = (data.decode("utf-8"))                                                                     
            option,parameter = getParameters(data)
            string = getQuery(option,parameter)
            reply = getFromWorker(string)
            connection.sendall(reply)
        except Exception as e:
            print(e)
            Logger.logger.error(e)
      
def startReader():
    readerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    readerSocket.bind(readerHost)
    print("Reader started!")
    Logger.logger.info("Reader started!")
    while readerSocket:
        readerSocket.listen()
        conn, addr = readerSocket.accept()
        print(f"Connected by {addr}")
        Logger.logger.info(f"Connected by {addr}")
        start_new_thread(multiThreadedConnection, (conn, ))

if __name__ == '__main__':
    start_new_thread(startReader())
    x = input()
    while x != "x":
        x = input()


def getQuery(option,parameter):
    string=""
    if option == "1":
        string = dbFunctions.createTable(dataset)
    elif option == "2":
        string = dbFunctions.Insert(code,value,dataset)
    elif option == "3":
        string = dbFunctions.GetLastValue(dataset, code)

    return string
