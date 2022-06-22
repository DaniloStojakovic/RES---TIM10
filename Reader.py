#reader
import Logger
import dbFunctions
import DataSets
import Code_Names
import CollectionDescription
import HistoricalCollection
import sys

class Reader:

    def startReader(self):
        while(true)
            print("Unesite zeljenu operaciju:\n1. Pretraga po kodu\n2. Pretraga po intervalu\n 3. Kraj")
            komanda = int(input())
            if komanda == 1:
                self.codeSearch()
            elif komanda == 2:
                self.intervalSearch()
            elif komanda == 3:
                break
            else :
                Logger.logger.error()

        def codeSearch(self):
            print("Izaberite kod:\n 1.CODE_ANALOG\n 2.CODE_DIGITAL\n 3.CODE_CUSTOM\n 4.CODE_LIMITSET\n 5.CODE_SINGLENOE\n 6.CODE_MULTIPLENODE\n 7.CODE_CONSUMER\n 8.CODE_SOURCE\n")
            code1 = int(input())
            if code1 == 1:
                code = "CODE_ANALOG"
            elif code1 == 2:
                code = "CODE_DIGITAL"
            elif code1 == 3:
                code = "CODE_CUSTOM"
            elif code1 == 4:
                code = "CODE_LIMITSET"
            elif code1 == 5:
                code = "CODE_SINGLENOE"
            elif code1 == 6:
                code = "CODE_MULTIPLENODE"
            elif code1 == 7:
                code = "CODE_CONSUMER"
            elif code1 == 8:
                code= "CODE_SOURCE"
            else:
                print("Uneli ste nepostojeci kod!\n\n")
                self.codeSearch()
            dataset = self.GetDataSet(code)

            retVal = db.getDataFromCode(code,dataset)
        

            return retVal

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
            db = DBFunctions()
            print("Unesi kod: ")
            code = str(input())

            if((code != "CODE_ANALOG") and (code != "CODE_DIGITAL") and (code !="CODE_CUSTOM") and (code != "CODE_LIMITSET") and (code != "CODE_SINGLENOE") and (code !="CODE_MULTIPLENODE")and(code!="CODE_CONSUMER")and(code!="CODE_SOURCE")):
                print("Nepostojeci kod.")
            
            dataset = self.getDataSet(code)
            
            print("Unesi pocetni interval: ")
            firstTimestamp = str(input())

            print("Unesi krajnji interval: ")
            secondTimestamp = str(input())

            retVal = db.getDataFromTimestamp(firstTimestamp,secondTimestamp,dataset)
            return retVal






