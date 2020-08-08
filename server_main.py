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
    def walking_out_directorys(self, root):
        """ walking out directory is a directory which will come back
        from the working directory to present directory"""
        path = os.getcwd()
        while True:
            if path == root:
                break
            else:
                try:
                    os.chdir('..')
                    path = os.getcwd()
                    if path == root:
                        break
                except OSError:
                    pass
    async def login_account(self, user_name, pass_word, addr, root):
        """here we can create login function
        attributes
        user_name: which is used to give the username of the user
        pass_word: which is used to give the password of the user
        addr: the address of the user"""
        count = 0
        try:
            if self.logined_list[addr] == 0 and self.logined_list[(user_name, pass_word)] == 1:
                for i in range(len(self.client_list)):
                    user_name_match = self.client_list[i][0]
                    pass_word_match = self.client_list[i][1]
                    if user_name == user_name_match and pass_word == pass_word_match:
                        message = 'login successful'
                        self.result.append(message)
                        message = message.encode()
                        tuple = (user_name, pass_word)
                        self.logined_list[tuple] = 1
                        self.temporary_clients[self.client_list[i]] = addr
                        self.logined_list[addr] = 1
                        try:
                            count = count+1
                            self.writer.write(message + '\n'.encode())
                            break
                        except:
                            pass
            elif self.logined_list[addr] == 1 and self.logined_list[(user_name, pass_word)] == 1:
                message = 'Already logined'
                self.result.append(message)
                message = message.encode()
                count = count + 1
                try:
                    self.writer.write(message + '\n'.encode())
                except:
                    pass
            if count == 0:
                message = 'login failed'
                self.result.append(message)
                message = message.encode()
                try:
                    self.writer.write(message + '\n'.encode())
                except:
                    pass
        except:
            message = 'logined Access deined'
            self.result.append(message)
            message = message.encode()
            try:
                self.writer.write(message + '\n'.encode())
            except:
                pass
    async  def register_account(self, user_name, pass_word, privilages, addr, root):
        """before login we have to register the account

        attributes
        user_name: which is used to give user_name of the user
        pass_word: which is used to give pass_word of the user
        privilages: privilages are used for to mentioned that user or admin"""
        if len(user_name) == 0:
            try:
                message = 'user_name should not be empty'
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
            for i in range(len(self.client_list)):
                user_name_match = self.client_list[i][0]
                pass_word_match = self.client_list[i][1]
                if user_name == user_name_match and pass_word == pass_word_match:
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
                        val = val + 1
                    except Exception:
                        pass
                if val == 0:
                    message = 'Account created succesfully'
                    self.result.append(message)
                    message = message.encode()
                    try:
                        self.writer.write(message + '\n'.encode())
                        self.logined_list[addr] = 1
                        self.logined_list[(user_name, pass_word)] = 1
                    except Exception:
                        pass
                    try:
                        path = os.getcwd()
                        try:
                            os.chdir(user_name)
                            path = os.getcwd()
                            client = (user_name, pass_word, privilages, path)
                            self.client_list.append(client)
                            self.temporary_clients[client] = addr
                            try:
                                os.chdir('..')
                            except OSError:
                                pass
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
                except Exception:
                    pass
        elif privilages != 'admin' and privilages != 'user':
            message = 'privilages must be either admin or user'
            self.result.append(message)
            message = message.encode()
            try:
                self.writer.write(message + '\n'.encode())
            except Exception:
                pass
    async def change_folder(self, Folder_name, addr, root):
        """here client can create a folder in the server
        attributes
        Folder_name: when we change the folder we have to mention the folder name"""
        path = self.walking_in_directorys(addr)
        try:
            os.chdir(Folder_name)
            new_path = os.getcwd()
            if new_path == root:
                try:
                    message = 'Cannot access outside of your folder'
                    message = message.encode()
                    self.writer.write(message + '\n'.encode())
                except Exception:
                    # print('client connection disconnected')
                    pass
            else:
                message = 'Folder changed successfully'
                self.result.append(message)
                message = message.encode()
                for i in range(len(self.client_list)):
                    if self.temporary_clients[self.client_list[i]] == addr:
                        deatils = self.client_list[i]
                        user_name = deatils[0]
                        pass_word = deatils[1]
                        previllages = deatils[2]
                        path = new_path
                        self.client_list[i] = (user_name, pass_word, previllages, path)
                        self.temporary_clients[self.client_list[i]] = addr
                        break
                try:
                    self.writer.write(message + '\n'.encode())
                except Exception:
                    # print('client connection disconnected')
                    pass
        except OSError:
            try:
                new_msg = 'No such Folder_name exits in the directory'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception:
                # print('client connection disconnected')
                pass
        self.walking_out_directorys(root)
    async def create_folder(self, Folder_name, addr, root):
        """here we can create the folder attributes
        Folder_name: when we create a folder we have to mentioned the foldername"""
        path = self.walking_in_directorys(addr)
        try:
            os.makedirs(Folder_name)
            try:
                new_msg = 'Folder created successfully'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception:
                # print('client connection disconnected')
                pass
        except OSError:
            try:
                new_msg = 'Folder_name already created try another name'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception:
                # print('client connection disconnected')
                pass
        self.walking_out_directorys(root)
    async def read_file(self, file_name, addr, root):
        """here we read a file from the server attributes
        file_name: before reading a file we have to mention the filename"""
        path = self.walking_in_directorys(addr)
        list = []
        count = -1
        for i in range(len(self.read_file_data)):
            try:
                if self.read_file_data[i][2] == file_name:
                    count = i
                    break
            except:
                pass
        if count != -1:
            try:
                try:
                    iter_obj = self.read_file_data[count][0]
                except:
                    print('error')
                string = ''
                for i in range(100):
                    try:
                        string = string + next(iter_obj)
                    except StopIteration:
                        break
                try:
                    length = self.read_file_data[count][1] - 100
                    if length <= 0:
                        self.read_file_data[count] = 0
                    else:
                        data = (iter_obj, length, file_name)
                        self.read_file_data[count] = data
                    if len(string) == 0:
                        string = 'File has readen completely'
                        self.result.append(string)
                    string = string.encode()
                    self.writer.write(string)
                    res = 'Data is readed'
                    self.result.append(res)
                except Exception:
                    print('client connection disconnected')
            except OSError:
                pass
        else:
            try:
                f = open(file_name, 'r')
                file_read = f.read()
                new_file_read = iter(file_read)
                string = ''
                count = 0
                for i in range(100):
                    try:
                        string = string + next(new_file_read)
                        count = count + 1
                    except StopIteration:
                        break
                f.close()
                if len(file_read) > 100:
                    try:
                        path = os.getcwd()
                    except OSError:
                        pass
                    data = (new_file_read, len(file_read)-100, file_name)
                    self.read_file_data.append(data)
                try:
                    if len(string) == 0:
                        string = 'content is missing in the file'
                    message = 'File reading is done'
                    self.result.append(message)
                    string = string.encode()
                    self.writer.write(string)
                except Exception:
                    # print('client connection disconnected')
                    pass
            except IOError:
                try:
                    new_msg = 'File does not exits in the directory'
                    self.result.append(new_msg)
                    new_msg = new_msg.encode()
                    self.writer.write(new_msg + '\n'.encode())
                except Exception:
                    # print('client connection disconnected')
                    pass
            self.walking_out_directorys(root)
    async def write_file(self, file_name, data, addr, root):
        """here we can write a file to the server

        attributes
        file_name: before writing a file we have to create a file
        data: whenwe create a file we can write the data into the file"""
        path = self.walking_in_directorys(addr)
        count = 0
        try:
            f = open(file_name, 'r+')
            message = 'file exists in the directory'
            f.close()
        except:
            count = 1
        if len(data) == 0 and count == 0:
            try:
                file_write = open(file_name, 'r+')
                file_write.truncate(0)
                file_write.close()
            except IOError:
                print('reading error')
        elif len(data) != 0:
            try:
                file_write = open(file_name, 'a')
                file_write.write(data)
                file_write.close()
            except IOError:
                print('reading error')
        if count == 0:
            try:
                new_msg = 'content succesfully written in the file'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception:
                # print('client connection disconnected')
                pass
        else:
            try:
                new_msg = 'New_file is created and content succesfully written in the file'
                self.result.append(new_msg)
                new_msg = new_msg.encode()
                self.writer.write(new_msg + '\n'.encode())
            except Exception:
                # print('client connection disconnected')
                pass
        self.walking_out_directorys(root)
    async def list_files(self, addr, root):
        """list file is used to print the existing files from the server"""
        nw_list = []
        list = []
        path = self.walking_in_directorys(addr)
        try:
            path = os.getcwd()
            list = os.listdir(path)
            if len(list) != 0:
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
                            string = string + 'Date_of_file and time_of_creation_of_file = '+ nw_list[i][j] + ' '
                    string = string + '\n'
                try:
                    new_msg = string.encode()
                    self.result.append(True)
                    self.writer.write(new_msg + '\n'.encode())
                except Exception:
                    # print('client connection disconnected')
                    pass
            else:
                try:
                    new_msg = 'NO Files present in the directory'
                    self.result.append(new_msg)
                    new_msg = new_msg.encode()
                    self.writer.write(new_msg + '\n'.encode())
                except Exception:
                    # print('client connection disconnected')
                    pass
        except OSError:
            print('os error')
        self.walking_out_directorys(root)
    async def delete_user(self, user_name, pass_word, addr):
        """here we can delete the user from the server
        attributes
        user_name: here we can write the user_name of the user
        pass_word: here we have to write the pass_word of the admin"""
        count = 0
        count1 = 0
        count2 = 0
        for i in range(len(self.client_list)):
            if self.temporary_clients[self.client_list[i]] == addr:
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
            except Exception:
                # print('client connection disconnected')
                pass
        elif count == 1:
            for i in range(len(self.client_list)):
                details = self.client_list[i]
                pass_word_match = details[1]
                if pass_word_match == pass_word:
                    count1 = count1 + 1
                    break
            if count1 == 0:
                try:
                    message = 'The password of the current admin not matching'
                    message = message.encode()
                    self.writer.write(message + '\n'.encode())
                except Exception:
                    # print('client connection disconnected')
                    pass
            elif count1 == 1:
                for i in range(len(self.client_list)):
                    details = self.client_list[i]
                    user_name_match = details[0]
                    if user_name == user_name_match:
                        delete_client = details
                        count2 = count2 + 1
                        break
                if count2 == 1:
                    self.client_list.remove(delete_client)
                    self.logined_list[addr] = 0
                    try:
                        message = 'User_name deleted succesfully'
                        message = message.encode()
                        self.writer.write(message + '\n'.encode())
                    except Exception:
                        # print('client connection disconnected')
                        pass
                else:
                    try:
                        message = 'User_name does not found'
                        message = message.encode()
                        self.writer.write(message + '\n'.encode())
                    except Exception:
                        # print('client connection disconnected')
                        pass

