#reader

import pickle
import socket
import sys

sys.path.append('../')

from Reader.CreateQuery import get_query
from _thread import start_new_thread

workerAddress = "127.0.0.1"
workerPort = 55000
workerHost = (workerAddress, workerPort)

readerAddress = "127.0.0.1" 
readerPort = 33000
readerHost = (readerAddress, readerPort)

def getFromWorker(string):
    workerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"connecting to Worker on [ADDR:PORT] : [{str(workerAddress)}:{str(workerPort)}]")
    logger.info(f"connecting to Worker on [ADDR:PORT] : [{str(workerAddress)}:{str(workerPort)}]")
    workerSocket.connect(workerHost)

    try:
        workerSocket.send(pickle.dumps(string.encode("utf-8")))
        reply = workerSocket.recv(1024)
        workerSocket.close()
        print(reply.decode("utf-8"))
        logger.info(reply.decode("utf-8"))
        return reply

    except Exception as e:
        workerSocket.close()
        print(e)
        logger.error(e)
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
            logger.error(e)
      
def startReader():
    readerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    readerSocket.bind(readerHost)
    print("Reader started!")
    logger.info("Reader started!")
    while readerSocket:
        readerSocket.listen()
        conn, addr = readerSocket.accept()
        print(f"Connected by {addr}")
        logger.info(f"Connected by {addr}")
        start_new_thread(multiThreadedConnection, (conn, ))

if __name__ == '__main__':
    start_new_thread(startReader())
    x = input()
    while x != "x":
        x = input()


def getQuery(option,parameter):
    string=""
    if option == "1":
        string = get_all()
    elif option == "2":
        string = get_by_month(parameter)
    elif option == "3":
        string = get_by_client_id(parameter)
    elif option == "4":
        string = get_by_city(parameter)
    elif option == "5":
        string = get_by_power_consumption_above(parameter)
    elif option == "6":
        string = get_by_power_consumption_below(parameter)

    return string

def get_all():
    return "SELECT * FROM meterReadings"

def get_by_month(month):
    sql_select = "SELECT * FROM meterReadings WHERE month = '" + month+"'"
    return sql_select

def get_by_power_consumption_above(value):
    sql_select = "SELECT * FROM meterReadings WHERE consumption > " + str(value)
    return sql_select

def get_by_power_consumption_below(value):
    sql_select = "SELECT * FROM meterReadings WHERE consumption < " + str(value)
    return sql_select

def get_by_city(city):
    return "SELECT * FROM meterReadings WHERE city = '" + city + "'"

def get_by_client_id(user_id):
    return "SELECT * FROM meterReadings WHERE user_id = "+str(user_id)