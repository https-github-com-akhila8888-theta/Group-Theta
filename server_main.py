"""importing modules"""
import os
import time
class server_class:
    """Creating server class"""
    def __init__(self, reader, writer, client_list,\
        logined_list, temporary_clients, read_file_data, result):
        """attributes
        reader: which the client is used to read a data from server
        writer: client is used to write the data from the server
        client_list: which is used to print the current clients in the server
        logined_list: which is used to print the current login list from the server
        temporary_clients: it will display the current clients in the server
        read_file: which is used to read the file from the server
        result: which is used to print the result"""
        self.reader = reader
        self.writer = writer
        self.client_list = client_list
        self.logined_list = logined_list
        self.temporary_clients = temporary_clients
        self.read_file_data = read_file_data
        self.result = result
    def walking_in_directorys(self, addr):
        """ walking directory shows that the present working directory"""
        for i in range(len(self.client_list)):
            if self.temporary_clients[self.client_list[i]] == addr:
                details = self.client_list[i]
                root = details[3]
        string = root.split('\\')
        try:
            path_string = os.getcwd()
        except OSError:
            pass
        path_string = path_string.split('\\')
        count = 0
        for i in range(len(path_string)):
            if string[i] == path_string[i]:
                count = count + 1
            else:
                break
        for i in range(count, len(string)):
            try:
                directory = string[i]
                os.chdir(directory)
            except OSError:
                pass
        try:
            val = os.getcwd()
        except OSError:
            pass
    
