#reader

import pickle
import socket
import sys

sys.path.append('../')

from Reader.CreateQuery import get_query
from _thread import start_new_thread


ReceiveHost = "127.0.0.1" 
ReceivePort = 40000

HistoricalHost="127.0.0.1"
HistoricalPort=60000

def get_from_historical(string):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HistoricalHost, HistoricalPort)
    print("connecting to Historical on address " + str(HistoricalHost)+":"+str(HistoricalPort)+"\n")
    sock.connect(server_address)

    try:
        sock.send(pickle.dumps(string.encode("utf-8")))
        reply = sock.recv(1024)
        sock.close()
        print(reply.decode("utf-8"))
        return reply

    except Exception as e:
        sock.close()
        print(e)
        return "ERROR"



def get_params(data):
    option=data.split(',')[0]
    parameter=data.split(',')[1]
    parameter=parameter[1:]
    return option,parameter

def multi_threaded_connection(connection): 
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                break
            data=(data.decode("utf-8"))                                                                     
            option,parameter=get_params(data)
            string=get_query(option,parameter)
            reply=get_from_historical(string)
            connection.sendall(reply)
        except Exception as e:
            print(e)
        
      
def start_reader():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((ReceiveHost, ReceivePort))
    print("Reader started!")
    while s:
        s.listen()
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        start_new_thread(multi_threaded_connection, (conn, ))

if __name__ == '__main__':
    start_new_thread(start_reader())
    x = input()
    while x != "x":
        x = input()


def get_query(option,parameter):
    string=""
    if option== "1":
        string= get_all()
    elif option== "2":
        string =get_by_month(parameter)
    elif option== "3":
        string =get_by_client_id(parameter)
    elif option== "4":
        string=get_by_city(parameter)
    elif option== "5":
        string = get_by_power_consumption_above(parameter)
    elif option== "6":
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