from contextlib import nullcontext
from unittest.mock import Mock
from LoadBalancer import LoadBalancer
import unittest


class TestLb(unittest.TestCase):

        '''def test_connection_recv(self):
                mock_connect=Mock()
                LoadBalancer.get_poruka(mock_connect)
                mock_connect.client.recv.assert_called()
                mock_connect.server_socket.close()
                mock_connect.client.close()'''
        
        def setUp(self):
                self.loadBalancer = LoadBalancer('localhost', 5555, 'round robin')

        def test_which_dataset(self):
                value = self.loadBalancer.which_dataset("CODE_ANALOG")
                check = 1
                self.assertEqual(check, value)

                value = self.loadBalancer.which_dataset("CODE_DIGITAL")
                check = 1
                self.assertEqual(check, value)
                
                value = self.loadBalancer.which_dataset("CODE_CUSTOM")
                check = 2
                self.assertEqual(check, value)

                value = self.loadBalancer.which_dataset("CODE_LIMITSET")
                check = 2
                self.assertEqual(check, value)

                value = self.loadBalancer.which_dataset("CODE_SINGLENOE")
                check = 3
                self.assertEqual(check, value)

                value = self.loadBalancer.which_dataset("CODE_MULTIPLENODE")
                check = 3
                self.assertEqual(check, value)

                value = self.loadBalancer.which_dataset("CODE_CONSUMER")
                check = 4
                self.assertEqual(check, value)

                value = self.loadBalancer.which_dataset("CODE_SOURCE")
                check = 4
                self.assertEqual(check, value)
        
        def test_connection_ipaddress(self):
                connection=LoadBalancer(10007,"122.0.0.1")
                self.assertRaises(OSError,connection.bind_socket,'122.0.0.1',10007)
                connection.server_socket.close()
                
        def test_connection_port(self):
                connection=LoadBalancer(9999999,"127.0.0.1")
                self.assertRaises(OverflowError,connection.bind_socket,'127.0.0.1',99999999999)
                connection.server_socket.close()
        
        def test_connection_port_type(self):
                konekcija=nullcontext
                self.assertRaises(ValueError,LoadBalancer.__init__,konekcija,"nesto",'127.0.0.1')
                

if __name__=="__main__":
    unittest.main()