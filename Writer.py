import pickle
import os
import Code_Names
import socket
from time import sleep
from WriterClass import WriterClass


ClientSocket2 = socket.socket()
host2 = 'localhost'
port2 = 5555
ClientSocket2.connect((host2, port2))





while True:

    print("Izaberite jednu od opcija: \n 1. Upis novih podataka \n 2. Paljenje i gasenje workera \n 3. Izlaz \n ")

    izbor = int(input())

    if izbor == 1:
        os.system('CLS')
        while True:
            print("Izaberite kod:\n 1.CODE_ANALOG\n 2.CODE_DIGITAL\n 3.CODE_CUSTOM\n 4.CODE_LIMITSET\n 5.CODE_SINGLENOE\n 6.CODE_MULTIPLENODE\n 7.CODE_CONSUMER\n 8.CODE_SOURCE\n");
            izbor2 = int(input())
            if izbor2 == 1:
                code = "CODE_ANALOG"
                print("Unesite value:")
                value= int(input())
                message = WriterClass(code, value)
                data_string = pickle.dumps(message)
                ClientSocket2.send(data_string)
                break;
            elif izbor2 == 2:
                code = "CODE_DIGITAL"
                print("Unesite value:")
                value= int(input()) 
                break;
            elif izbor2 == 3:
                code = "CODE_CUSTOM"
                print("Unesite value:")
                value= int(input())
                break;
            elif izbor2 == 4:
                code = "CODE_LIMITSET"
                print("Unesite value:")
                value= int(input())
                break;
            elif izbor2 == 5:
                code = "CODE_SINGLENOE"
                print("Unesite value:")
                value= int(input())
                break;
            elif izbor2 == 6:
                code = "CODE_MULTIPLENODE"
                print("Unesite value:")
                value= int(input())
                break;
            elif izbor2 == 7:
                code = "CODE_CONSUMER"
                print("Unesite value:")
                value= int(input())
                break;
                print(code)
            elif izbor2 == 8:
                code= "CODE_SOURCE"
                print("Unesite value:")
                value= int(input())
                break;
            else:
                print("Izaberite redni broj zeljene koda!\n\n")


        
        
    elif izbor == 2:
        os.system('CLS')
        #ovde radimo paljenje i gasenje
        print("2")
        
    elif izbor == 3:
        os.system('CLS')
        print("3")
        break;
    else:
        print("Izaberite redni broj zeljene opcije(od 1 do 3)!\n\n")









