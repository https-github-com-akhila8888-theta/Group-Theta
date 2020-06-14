"""importing modules"""
import asyncio
import unittest
from server_main import server_class
from assign3_client import client_class
class servertesting(unittest.TestCase):

    def setUp(self):
        """here we can setup the commands"""

        pass

    def test_register(self):
        """here we can test the register function"""
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.register_account('vinay', '$vinay123', 'admin', '121.0.0.1'))
        asyncio.run(obj.register_account('vinay', '$vinay123', 'admin', '121.0.0.1'))
        asyncio.run(obj.register_account('ramesh', 'ramesh88', 'usser', '121.0.0.1'))
        expected_results = ['Account created succesfully',
                            'Account already created',
                            'privilages must be either admin or user'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_login(self):
        """here we can test the login function"""
        obj = server_class([], [], [], {}, {}, {}, [])
        client = ('vinay', '$vinay123', 'admin')
        obj.logined_list['121.0.0.2'] = 0
        obj.client_list.append(client)
        asyncio.run(obj.login_account('vinay', '$vinay', '121.0.0.2'))
        asyncio.run(obj.login_account('vinay', '$vinay123', '121.0.0.2'))
        asyncio.run(obj.login_account('vinay', '$vinay123', '121.0.0.2'))
        expected_results = ['login failed',
                            'login successful',
                            'logined already'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_create_folder(self):
        """testing the creating folder in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.create_folder('sai'))
        asyncio.run(obj.create_folder('sai'))
        expected_results = ['Folder created successfully',
                            'Folder_name already created try another name'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_change_folder(self):
        """testing the changing folder in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.create_folder('sai'))
        asyncio.run(obj.change_folder('sai'))
        asyncio.run(obj.change_folder('ramesh'))
        expected_results = ['Folder created successfully',
                            'Folder changed successfully',
                            'No such Folder_name exits in the directory'
                            ]
        self.assertListEqual(obj.result, expected_results)
    def test_list_files(self):
        """testing the list files in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.list_files())
        expected_result = [True]
        self.assertListEqual(obj.result, expected_result)
    def test_write_file(self):
        """testing the write files in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.write_file('sample.txt', 'saidattu'))
        asyncio.run(obj.write_file('sample.txt', 'is a good'))
        expected_results = ['New_file is created and content succesfully written in the file',
                            'content succesfully written in the file'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_read_file(self):
        """testing the reading files in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        asyncio.run(obj.write_file('sample.txt', 'saidattu'))
        asyncio.run(obj.read_file('sample.txt'))
        asyncio.run(obj.read_file('new_sample.txt'))
        expected_results = ['New_file is created and content succesfully written in the file',
                            'File reading is done',
                            'File does not exits in the directory'
                           ]
        self.assertListEqual(obj.result, expected_results)
    class client_testing(unittest.TestCase):
        def test_quit(self):
            """here we can quit the commands from the server"""
            obj = client_class('121.0.0.1', 8080, [], [])
            obj.logout()
            expected_result = ['logout successfully done']
            self.assertListEqual(expected_result, obj.result)
        def test_commands_clear(self):
            """here we can clear the commands from the server"""
            obj = client_class('121.0.0.1', 8080, [], [])
            obj.commands_clear()
            expected_result = ['commands cleared']
            self.assertListEqual(expected_result, obj.result)


if __name__ == '__main__':
    unittest.main()
