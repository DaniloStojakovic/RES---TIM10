import pickle
import os
import Code_Names
import socket
from time import sleep
from WriterClass import WriterClass
import Logger




ClientSocket2 = socket.socket()
host2 = 'localhost'
port2 = 5555
ClientSocket2.connect((host2, port2))
Logger.logger.info("Writer: Writer komponenta se konektovala na load balancer")


class Writer:

    def ZaSlanje(code):
        print("Unesite value:")
        value= int(input())
        poruka = WriterClass(code, value)
        zaSlanje = pickle.dumps(poruka)
        ClientSocket2.send(zaSlanje)

    def SlanjeStanja(upaljen, i):
        poruka2 = WriterClass(upaljen, i)
        zaSlanje2 = pickle.dumps(poruka2)
        ClientSocket2.send(zaSlanje2)

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
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_ANALOG i value je odabran i poslat")
                    break
                elif izbor2 == 2:
                    code = "CODE_DIGITAL"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_DIGITAL i value je odabran i poslat")
                    break
                elif izbor2 == 3:
                    code = "CODE_CUSTOM"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_CUSTOM i value je odabran i poslat")
                    break
                elif izbor2 == 4:
                    code = "CODE_LIMITSET"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_LIMITSET i value je odabran i poslat")
                    break
                elif izbor2 == 5:
                    code = "CODE_SINGLENOE"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_SINGLENOE i value je odabran i poslat")
                    break
                elif izbor2 == 6:
                    code = "CODE_MULTIPLENODE"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_MULTIPLENODE i value je odabran i poslat")
                    break
                elif izbor2 == 7:
                    code = "CODE_CONSUMER"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_CONSUMER i value je odabran i poslat")
                    break
                elif izbor2 == 8:
                    code= "CODE_SOURCE"
                    ZaSlanje(code)
                    Logger.logger.info("Writer: izabrani code je CODE_SOURCE i value je odabran i poslat")
                    break
                else:
                    print("Izaberite redni broj zeljene koda!\n\n")


            
            
        elif izbor == 2:
            os.system('CLS')
            while True:
                print("Izaberite jednu od opcija: \n 1.Paljenje workera \n 2.Gasenje workera \n")
                izbor3 = int(input())
                if izbor3 == 1:
                    os.system('CLS')
                    print("Izaberite redni broj workera koji zelite da upalite: \n")
                    izbor4= int(input())
                    if(izbor4 < 0):
                        print("Morate uneti broj veci 0!\n")
                        continue
                    else:
                        upaljen = "ON"
                        SlanjeStanja(upaljen, izbor4) 
                        Logger.logger.info("Writer: Izabrano je paljenje workera!")             
                    break
                elif izbor3 == 2:
                    os.system('CLS')
                    print("Izaberite redni broj workera koji zelite da ugasite: \n")
                    izbor4= int(input())
                    if(izbor4 < 0):
                        print("Morate uneti broj veci od 0!\n")
                        continue
                    else:
                        upaljen = "OFF"
                        SlanjeStanja(upaljen, izbor4) 
                        Logger.logger.info("Writer: Izabrano je gasenje workera!")
                    break
                else:
                    print("Morate izabrate ili paljenje workera pod 1 ili gasenje workera pod 2!!! \n")
        
            
            
        elif izbor == 3:
            os.system('CLS')
            print("Gasenje programa!\n")
            Logger.logger.info("Writer: Program se gasi!")
            break
        else:
            print("Izaberite redni broj zeljene opcije(od 1 do 3)!\n\n")

if __name__ == "__main__":  # ovo ispod se nece pozvati pri importovanju
    Writer1 = Writer()