import asyncio
import unittest
from server_main import server_class
from ass3_client import client_class
class servertesting(unittest.TestCase):

    def setUp(self):
        """Initializing the variables"""

        pass

    def test_register(self):
        """testing the register in directory """
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.register_account('vinay', '$vinay123', 'admin', '121.0.0.1'))
        asyncio.run(obj.register_account('vinay', '$vinay123', 'admin', '121.0.0.1'))
        asyncio.run(obj.register_account('ramesh', 'ramesh88', 'usser', '121.0.0.1'))
        expected_results = ['Account created succesfully',
                            'Account already created',
                            'privilages must be either admin or user'
                           ]
        self.assertListEqual(obj.result, expected_results)
        
        
        
        
if __name__ == '__main__':
    unittest.main()
