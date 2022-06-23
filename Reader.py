#reader
import Logger
import dbFunctions
import DataSets
import Code_Names
import CollectionDescription
import HistoricalCollection
import sys
from datetime import datetime

class Reader:

    def startReader(self):
        while(True):
            Logger.logger.info('Rider: pokretanje ridera')
            print("Unesite zeljenu operaciju:\n1. Pretraga po kodu\n2. Pretraga po intervalu\n 3. Kraj")
            komanda = int(input())
            if komanda == 1:
                Logger.logger.info('Rider: izabrana je opcija pretrage po kodu')
                self.codeSearch()
            elif komanda == 2:
                Logger.logger.info('Rider: izabrana je opcija pretrage po intervalu')
                self.intervalSearch()
            elif komanda == 3:
                Logger.logger.info('Rider: izlazak iz ridera')
                break
            else :
                Logger.logger.info('Rider: izabrana je nemoguca opcija!')
                print("Uneli ste nemogucu operaciju!")
                self.startReader()

    def codeSearch(self):
        print("Izaberite kod:\n 1.CODE_ANALOG\n 2.CODE_DIGITAL\n 3.CODE_CUSTOM\n 4.CODE_LIMITSET\n 5.CODE_SINGLENOE\n 6.CODE_MULTIPLENODE\n 7.CODE_CONSUMER\n 8.CODE_SOURCE\n")
        code1 = int(input())
        if code1 == 1:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_ANALOG')
            code = "CODE_ANALOG"
        elif code1 == 2:
           Logger.logger.info('Rider: codeSearch: izabran je CODE_DIGITAL')
           code = "CODE_DIGITAL"
        elif code1 == 3:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_CUSTOM')
            code = "CODE_CUSTOM"
        elif code1 == 4:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_LIMITSET')
            code = "CODE_LIMITSET"
        elif code1 == 5:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_SINGLENOE')
            code = "CODE_SINGLENOE"
        elif code1 == 6:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_MUTLIPLENODE')
            code = "CODE_MULTIPLENODE"
        elif code1 == 7:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_CONSUMER')
            code = "CODE_CONSUMER"
        elif code1 == 8:
            Logger.logger.info('Rider: codeSearch: izabran je CODE_SOURCE')
            code= "CODE_SOURCE"
        else:
            Logger.logger.info('Rider: codeSearch: izabran je nepostojeci kod!')
            print("Uneli ste nepostojeci kod!\n\n")
            self.codeSearch()
        dataset = self.GetDataSet(code)
        retVal = dbFunctions.DBFunctions.GetValuesByCode(dataset, code)
        if retVal:
            Logger.logger.info('Rider: codeSearch: Vrijednosti {code}:\n')
            print(f"Vrijednosti {code}:\n")
            for value in retVal:
                Logger.logger.info("Rider: codeSearch: {value}:\n")
                print(value)
        else:
            Logger.logger.info('Rider: codeSearch: Nema vrijednosti za uneseni kod!')
            print("Nema vrijednosti za uneseni kod")
       

    def GetDataSet(self, code ):
        if code == "CODE_ANALOG" or code == "CODE_DIGITAL" :
            return 1
        elif code == "CODE_CUSTOM" or code == "CODE_LIMITSET" :
            return 2
        elif code ==  "CODE_SINGLENOE" or code =="CODE_MULTIPLENODE" :
            return 3
        elif code == "CODE_CONSUMER" or code == "CODE_SOURCE" :
            return 4


    def intervalSearch(self):
        print("Izaberite kod:\n 1.CODE_ANALOG\n 2.CODE_DIGITAL\n 3.CODE_CUSTOM\n 4.CODE_LIMITSET\n 5.CODE_SINGLENOE\n 6.CODE_MULTIPLENODE\n 7.CODE_CONSUMER\n 8.CODE_SOURCE\n")
        code1 = int(input())
        if code1 == 1:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_ANALOG')
            code = "CODE_ANALOG"
        elif code1 == 2:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_DIGITAL')
            code = "CODE_DIGITAL"
        elif code1 == 3:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_CUSTOM')
            code = "CODE_CUSTOM"
        elif code1 == 4:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_LIMITSET')
            code = "CODE_LIMITSET"
        elif code1 == 5:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_SINGLENOE')
            code = "CODE_SINGLENOE"
        elif code1 == 6:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_MULTIPLENODE')
            code = "CODE_MULTIPLENODE"
        elif code1 == 7:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_CONSUMER')
            code = "CODE_CONSUMER"
        elif code1 == 8:
            Logger.logger.info('Rider: intervalSearch: izabran je CODE_SOURCE')
            code = "CODE_SOURCE"
        else:
            Logger.logger.info('Rider: intervalSearch: izabran je nepostojeci kod!')
            print("Uneli ste nepostojeci kod!\n\n")
            self.intervalSearch()
            
        dataset = self.GetDataSet(code)
           
        time1 = self.TimeConverter()
        time2 = self.TimeConverter()
        retVal = dbFunctions.DBFunctions.GetDataByCode(dataset, code,time1, time2)
        if retVal:
            Logger.logger.info(f"Rider: intervalSearch: Vrijednosti {code} upisane izmedju {time1} i {time2}:\n")
            print(f"Vrijednosti {code} upisane izmedju {time1} i {time2}:\n")
            for value in retVal:
                Logger.logger.info(f"Rider: intervalSearch: {value}:\n")
                print(value)
        else:
            Logger.logger.info('Rider: codeSearch: Nema vrijednosti za uneseni kod!')
            print("Nema vrijednosti unesenog koda u unesenom vremenskom intervalu")

        
        
        
        
    def TimeConverter(self):
        timeFrom = input("Unesi vremenski interval u formatu Y-m-d H:M:S \nod:")
        try:
            date = datetime.strptime(timeFrom, '%Y-%m-%d %H:%M:%S')
            Logger.logger.info('Rider: TimeConverter: datum je uspjesno parsiran')
            return date
        except:
            Logger.logger.error('Rider: TimeConverter: unos se ne moze pretvoriti u datetime format!')
            print("greska")
            self.timeFromFunction()

chida = Reader()
chida.startReader()

if __name__ == "__main__":  # ovo ispod se nece pozvati pri importovanju
    reader1 = Reader()
    reader1.startReader()