import os
import sys
import time
class server_class:
    """Creating server class"""
    def __init__(self,reader,writer,client_list,logined_list,temporary_clients,read_file_data,result):
        """Initializing the variables"""
        self.reader = reader
        self.writer = writer
        self.client_list = client_list
        self.logined_list = logined_list
        self.temporary_clients = temporary_clients
        self.read_file_data = read_file_data
        self.result = result
    async  def register_account(self,user_name,pass_word,privilages,addr):
        """register account"""
        if len(user_name) == 0 :
            try:
                message = 'user_name should not be empty'
                self.result.append(message) 
                message = message.encode()   
                self.writer.write(message + '\n'.encode())
            except:
                pass
        elif(len(pass_word) == 0) :
            try:
                message = 'user_name should not be empty'
                self.result.append(message) 
                message = message.encode()    
                self.writer.write(message + '\n'.encode())
            except:
                pass
        elif(privilages == 'admin' or privilages == 'user'):
            count = 0
            client =  ( user_name , pass_word ,privilages)
            for i in range(len(self.client_list)):
                user_name_match = self.client_list[i][0]
                pass_word_match = self.client_list[i][1]
                if( user_name == user_name_match and pass_word == pass_word_match):
                    count = count + 1
            if count == 0:
                val = 0
                try:
                    os.makedirs(user_name)
                except OSError:
                    try:
                        message = 'Try another user_name'
                        self.result.append(message) 
                        message = message.encode()   
                        self.writer.write(message + '\n'.encode())
                        val = val +1
                    except:
                        pass
                if val == 0:
                    message = 'Account created succesfully'
                    self.result.append(message) 
                    message = message.encode()    
                    try:
                        self.writer.write(message + '\n'.encode())
                        self.logined_list [addr]  = 1
                    except:
                        pass
                    self.client_list.append(client)
                    self.temporary_clients[client] = addr
                    try:
                        path = os.getcwd()
                        try:
                            os.chdir(user_name)
                        except OSError:
                            print('Directory not changed')
                    except OSError:
                        print('Directory not found')
            elif count > 0:
                message = 'Account already created'
                self.result.append(message) 
                message = message.encode()   
                try:
                    self.writer.write(message + '\n'.encode())
                except:
                    pass
        elif (privilages != 'admin' and privilages != 'user' ):
            message = 'privilages must be either admin or user'
            self.result.append(message) 
            message = message.encode()    
            try:
                self.writer.write(message + '\n'.encode())
            except:
                pass        
