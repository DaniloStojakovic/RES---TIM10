import unittest
from Worker import Worker
import dbFunctions
from WorkerProperty import WorkerProperty

class TestWorker(unittest.TestCase):

    def setUp(self):
        self.worker = Worker(1)

        dbFunctions.DBFunctions.createTable(1)
        dbFunctions.DBFunctions.Insert("CODE_ANALOG",120 ,0 )
        dbFunctions.DBFunctions.Insert("CODE_DIGITAL",80,0 )

    def test_Validation(self):
        value = self.worker.Validation(WorkerProperty("CODE_DIGITAL", 81))
        check = True
        self.assertEqual(check, value)

        value = self.worker.Validation(WorkerProperty("CODE_ANALOG", 80))
        check = True
        self.assertEqual(check, value)

        value = self.worker.Validation(WorkerProperty("CODE_ANALOG", 121))
        check = False
        self.assertEqual(check, value)

    def test_Deadband(self):
        value = self.worker.Deadband(4,20)
        check = True
        self.assertEqual(check, value)
        
        value = self.worker.Deadband(80,81)
        check = False
        self.assertEqual(check, value)

        value = self.worker.Deadband(65,64)
        check = False
        self.assertEqual(check, value)

        value = self.worker.Deadband(150,90)
        check = True
        self.assertEqual(check, value)

    def test_GetDataSet(self):
        value = self.worker.GetDataSet("CODE_ANALOG")
        check = 1
        self.assertEqual(check, value)

        value = self.worker.GetDataSet("CODE_DIGITAL")
        check = 1
        self.assertEqual(check, value)
         
        value = self.worker.GetDataSet("CODE_CUSTOM")
        check = 2
        self.assertEqual(check, value)

        value = self.worker.GetDataSet("CODE_LIMITSET")
        check = 2
        self.assertEqual(check, value)

        value = self.worker.GetDataSet("CODE_SINGLENOE")
        check = 3
        self.assertEqual(check, value)

        value = self.worker.GetDataSet("CODE_MULTIPLENODE")
        check = 3
        self.assertEqual(check, value)

        value = self.worker.GetDataSet("CODE_CONSUMER")
        check = 4
        self.assertEqual(check, value)

        value = self.worker.GetDataSet("CODE_SOURCE")
        check = 4
        self.assertEqual(check, value)
        
if __name__ == '__main__':
    unittest.main()