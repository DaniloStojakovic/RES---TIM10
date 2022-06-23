from Reader import Reader
import unittest

class TestReader(unittest.TestCase):

    def setUp(self):
        self.reader = Reader()

    def test_GetDataSet(self):
        value = self.reader.GetDataSet("CODE_ANALOG")
        check = 1
        self.assertEqual(check, value)

        value = self.reader.GetDataSet("CODE_DIGITAL")
        check = 1
        self.assertEqual(check, value)
         
        value = self.reader.GetDataSet("CODE_CUSTOM")
        check = 2
        self.assertEqual(check, value)

        value = self.reader.GetDataSet("CODE_LIMITSET")
        check = 2
        self.assertEqual(check, value)

        value = self.reader.GetDataSet("CODE_SINGLENOE")
        check = 3
        self.assertEqual(check, value)

        value = self.reader.GetDataSet("CODE_MULTIPLENODE")
        check = 3
        self.assertEqual(check, value)

        value = self.reader.GetDataSet("CODE_CONSUMER")
        check = 4
        self.assertEqual(check, value)

        value = self.reader.GetDataSet("CODE_SOURCE")
        check = 4
        self.assertEqual(check, value)

if __name__ == '__main__':
    unittest.main()