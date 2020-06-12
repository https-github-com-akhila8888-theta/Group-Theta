import os
import sys
import time
class server_class:
    """Creating server class"""
    def __init__(self, reader, writer, client_list, logined_list, temporary_clients, read_file_data, result):
        """Initializing the variables"""
        self.reader = reader
        self.writer = writer
        self.client_list = client_list
        self.logined_list = logined_list
        self.temporary_clients = temporary_clients
        self.read_file_data = read_file_data
        self.result = result
    async def login_account(self, user_name, pass_word, addr):
        """login account"""
        count = 0
        if self.logined_list[addr] == 0:
            for i in range(len(self.client_list)):
                user_name_match = self.client_list[i][0]
                pass_word_match = self.client_list[i][1]
                if (user_name == user_name_match and pass_word == pass_word_match):
                    message = 'login successful'
                    self.result.append(message)
                    message = message.encode()
                    tuple = (user_name, pass_word)
                    self.logined_list[tuple] = 1
                    self.temporary_clients = addr
                    self.logined_list[addr] = 1
                    try:
                        count = count+1
                        self.writer.write(message + '\n'.encode())
                        break
                    except:
                        pass
                    try:
                        path = os.getcwd()
                        try:
                            os.chdir(user_name)
                        except OSError:
                            pass
                    except OSError:
                        pass
            if count == 0:
                message = 'login failed'
                self.result.append(message)
                message = message.encode()
                try:
                    self.writer.write(message + '\n'.encode())
                except:
                    pass
        else:
            message = 'logined already'
            self.result.append(message)
            message = message.encode()
            try:
                self.writer.write(message + '\n'.encode())
            except:
                pass
    async  def register_account(self, user_name, pass_word, privilages, addr):
        """register account"""
        if len(user_name) == 0:
            try:
                message ='user_name should not be empty'
                self.result.append(message)
                message = message.encode()
                self.writer.write(message + '\n'.encode())
            except:
                pass
        elif len(pass_word) == 0:
            try:
                message = 'user_name should not be empty'
                self.result.append(message) 
                message = message.encode()    
                self.writer.write(message + '\n'.encode())
            except:
                pass
        elif privilages == 'admin' or privilages == 'user':
            count = 0
            client = (user_name, pass_word, privilages)
            for i in range(len(self.client_list)):
                user_name_match = self.client_list[i][0]
                pass_word_match = self.client_list[i][1]
                if (user_name == user_name_match and pass_word == pass_word_match):
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
                        self.logined_list[addr] = 1
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
        elif (privilages != 'admin' and privilages != 'user'):
            message = 'privilages must be either admin or user'
            self.result.append(message) 
            message = message.encode()    
            try:
                self.writer.write(message + '\n'.encode())
            except:
                pass        
    async def change_folder(self, Folder_name):
        """changing the folder"""
        path = os.getcwd()
        try:
            os.chdir(Folder_name)
            message = 'Folder changed successfully'
            self.result.append(message)
            message = message.encode()
            try:
                self.writer.write(message + '\n'.encode())
            except Exception as e:
                # print('client connection disconnected')
                pass
        except OSError:
            try:
                new_msg = 'No such Folder_name exits in the directory'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception as e:
                # print('client connection disconnected')
                pass
    async def create_folder(self, Folder_name):
        """creating the folder"""
        try:
            os.makedirs(Folder_name)
            try:
                new_msg = 'Folder created successfully'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception as e:
                # print('client connection disconnected')
                pass
        except OSError:
            try:
                new_msg = 'Folder_name already created try another name'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception as e:
                # print('client connection disconnected')
                pass
   
    
    async def list_files(self):
        """list files"""
        nw_list = []
        try:
            path = os.getcwd()
            list = os.listdir(path)
            string = ''
            for i in range(len(list)):
                size = os.path.getsize(list[i])
                date = time.ctime(os.path.getctime(list[i]))
                data = (list[i], size, date)
                nw_list.append(data)
            for i in range(len(nw_list)):
                for j in range(len(nw_list[i])):
                    if j == 0:
                        string = string + 'Name_of_file = ' + nw_list[i][j] + ' '
                    elif j == 1:
                         string = string + 'size_of_file = ' + str(nw_list[i][j]) + 'bytes  '
                    elif j == 2:
                         string = string + 'Date_of_file and time_of_creation_of_file = ' + nw_list[i][j] + ' '
                string = string + '\n'
            try:
                new_msg = string.encode()
                self.result.append(True)
                self.writer.write(new_msg + '\n'.encode())
            except Exception as e:
                # print('client connection disconnected')
                pass
        except OSError:
            self.result.append(False)
            print('os error')
    async def delete_user(self, user_name, pass_word, addr):
        """deleting users"""
        count = 0
        count1 = 0
        count2 = 0
        for i in range(len(self.client_list)):
            if(self.temporary_clients[self.client_list[i]] == addr):
                details = self.client_list[i]
                previllage = details[2]
                if previllage == 'admin':
                    count = count + 1
                    break
        if count == 0:
            try:
                message = 'The client is not admin'
                message = message.encode()
                self.writer.write(message + '\n'.encode())
            except Exception as e:
                # print('client connection disconnected')
                pass
        elif count == 1:
            for i in range(len(self.client_list)):
                details = self.client_list[i]
                pass_word_match = details[1]
                if (pass_word_match == pass_word):
                    count1 = count1 + 1
                    break
            if count1 == 0:
                try:
                    message = 'The password of the current admin not matching'
                    message = message.encode()
                    self.writer.write(message + '\n'.encode())
                except Exception as e:
                    # print('client connection disconnected')
                    pass
            elif count1 == 1:
                for i in range(len(self.client_list)):
                    details = self.client_list[i]
                    user_name_match = details[0]
                    if (user_name == user_name_match):
                        delete_client = details
                        count2 = count2 + 1
                        break
                if count2 == 1:
                    self.client_list.remove(delete_client)
                    try:
                        message = 'User_name deleted succesfully'
                        message = message.encode()
                        self.writer.write(message + '\n'.encode())
                    except Exception as e:
                        # print('client connection disconnected')
                        pass
                else:
                    try:
                        message = 'User_name does not found'
                        message = message.encode()
                        self.writer.write(message + '\n'.encode())
                    except Exception as e:
                        # print('client connection disconnected')
                        pass
