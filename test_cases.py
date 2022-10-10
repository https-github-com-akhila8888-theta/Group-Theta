"""importing modules"""
import asyncio
import unittest
import os
from server_main import server_class
from assign3_client import client_class
class servertesting(unittest.TestCase):
    def setUp(self):
        """here we can setup the commands"""
        pass

    def test_register(self):
        """here we can test the register function"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        asyncio.run(obj.register_account('vinay', '$vinay123', 'admin', '121.0.0.1', list[0]))
        asyncio.run(obj.register_account('vinay', '$vinay123', 'admin', '121.0.0.1', list[0]))
        asyncio.run(obj.register_account('ramesh', 'ramesh88', 'usser', '121.0.0.1', list[0]))
        expected_results = ['Account created succesfully',
                            'Account already created',
                            'privilages must be either admin or user'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_login(self):
        """here we can test the login function"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        obj.logined_list['121.0.0.2'] = 0
        obj.logined_list[('vinay', '$vinay123')] = 1
        client = ('vinay', '$vinay123', 'admin', path)
        obj.client_list.append(client)
        asyncio.run(obj.login_account('vinay', '$vinay', '121.0.0.2', list[0]))
        asyncio.run(obj.login_account('vinay', '$vinay123', '121.0.0.2', list[0]))
        asyncio.run(obj.login_account('vinay', '$vinay123', '121.0.0.2', list[0]))
        expected_results = ['logined Access deined',
                            'login successful',
                            'Already logined'
                            ]
        self.assertListEqual(obj.result, expected_results)
    def test_create_folder(self):
        """testing the creating folder in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        asyncio.run(obj.register_account('kiran', '&kiran', 'user', '121.0.0.3', list[0]))
        try:
            os.chdir('kiran')
        except:
            pass
        asyncio.run(obj.create_folder('work', '121.0.0.3', list[0]))
        asyncio.run(obj.create_folder('work', '121.0.0.3', list[0]))
        expected_results = ['Account created succesfully',
                            'Folder created successfully',
                            'Folder_name already created try another name'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_write_file(self):
        """testing the write files in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        asyncio.run(obj.register_account('ramesh', 'coder', 'user', '121.0.0.4', list[0]))
        try:
            os.chdir('ramesh')
        except:
            pass
        asyncio.run(obj.write_file('sample.txt', 'saidattu', '121.0.0.4', path))
        asyncio.run(obj.write_file('sample.txt', 'is a good', '121.0.0.4', path))
        expected_results = ['Account created succesfully',
                            'New_file is created and content succesfully written in the file',
                            'content succesfully written in the file'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_change_folder(self):
        """testing the changing folder in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        asyncio.run(obj.register_account('akhil', 'love', 'user', '121.0.0.5', list[0]))
        try:
            os.chdir('akhil')
        except:
            pass
        asyncio.run(obj.create_folder('data', '121.0.0.5', list[0]))
        asyncio.run(obj.change_folder('data', '121.0.0.5', list[0]))
        asyncio.run(obj.write_file('work.txt', 'presentation is needed', '121.0.0.5', path))
        asyncio.run(obj.change_folder('..', '121.0.0.5', list[0]))
        expected_results = ['Account created succesfully',
                            'Folder created successfully',
                            'Folder changed successfully',
                            'New_file is created and content succesfully written in the file',
                            'Folder changed successfully'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_list_files(self):
        """testing the list files in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        asyncio.run(obj.register_account('andrew', 'hamming', 'user', '121.0.0.7', list[0]))
        try:
            os.chdir('andrew')
        except:
            pass
        asyncio.run(obj.write_file('sample.txt', 'saidattu', '121.0.0.7', path))
        asyncio.run(obj.list_files('121.0.0.7', path))
        asyncio.run(obj.register_account('sophia', '&queen', 'user', '121.0.0.8', list[0]))
        try:
            os.chdir('sophia')
        except:
            pass
        asyncio.run(obj.list_files('121.0.0.8', path))
        expected_results = ['Account created succesfully',
                            'New_file is created and content succesfully written in the file',
                            True,
                            'Account created succesfully',
                            'NO Files present in the directory'
                           ]
        self.assertListEqual(obj.result, expected_results)
    def test_read_file(self):
        """testing the reading files in directory"""
        obj = server_class([], [], [], {}, {}, {}, [])
        path = os.getcwd()
        list = []
        list.append(path)
        asyncio.run(obj.register_account('koushik', 'ilovecomputer', 'user', '121.0.0.9', list[0]))
        try:
            os.chdir('koushik')
        except:
            pass
        asyncio.run(obj.write_file('sample.txt', 'hello world', '121.0.0.9', path))
        asyncio.run(obj.read_file('sample.txt', '121.0.0.9', path))
        asyncio.run(obj.read_file('hello.txt', '121.0.0.9', path))
        expected_results = ['Account created succesfully',
                            'New_file is created and content succesfully written in the file',
                            'File reading is done',
                            'File does not exits in the directory'
                           ]
        self.assertListEqual(obj.result, expected_results)
class client_testing(unittest.TestCase):
    def test_commands_clear(self):
        """here we can clear the commands from the server"""
        obj = client_class('121.0.0.12', 8080, [], [])
        obj.commands_clear()
        expected_result = ['commands cleared']
        self.assertListEqual(expected_result, obj.result)
    def test_commands_issued(self):
        """here we can quit the commands from the server"""
        obj = client_class('121.0.0.14', 8080, [], [])
        obj.commands_issued()
        expected_result = ['Commands are issued']
        self.assertListEqual(expected_result, obj.result)

if __name__ == '__main__':
    unittest.main()
