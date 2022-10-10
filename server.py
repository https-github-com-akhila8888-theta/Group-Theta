"""importing modules"""
import asyncio
import queue
import os
from server_main import server_class
client_list = []
logined_list = {}
temporary_clients = {}
read_file_data = []
queue_data = queue.Queue()
result = []
async def new_echo_handle(reader, writer):
    server = server_class(reader, writer, client_list, logined_list,\
        temporary_clients, read_file_data, result)
    """attributes
    reader: which the client is used to read a data from server
    writer: client is used to write the data from the server
    client_list: which is used to print the current clients in the server
    logined_list: which is used to print the current login list from the server
    temporary_clients: it will display the current clients in the server
    read_file: which is used to read the file from the server
    result: which is used to print the result"""
    addr = writer.get_extra_info('peername')
    logined_list[addr] = 0
    try:
        root = os.getcwd()
    except OSError:
        pass
    message = f"{addr} is connected !!!!"
    print(message)
    while True:
        try:
            data = await reader.read(100)
            nw_data = data.decode()
            print(nw_data)
            queue_data.put(data)
            while queue_data.empty() == 0:
                queue_data.get()
                message = data.decode().split()
                if message[0] == 'login':
                    # here we can login from cilent to server
                    if len(message) != 3:
                        try:
                            new_msg = 'Error occured in syntax of login data'\
                            'It must login user_name password'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            print('client connection disconnected')
                    else:
                        addr = writer.get_extra_info('peername')
                        await server.login_account(message[1], message[2], addr, root)
                elif message[0] == 'register':
                    """we have to register from client to server"""
                    if len(message) != 4:
                        try:
                            new_msg = 'Error occured in syntax of register data'\
                            'It must login user_name password privilages'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        addr = writer.get_extra_info('peername')
                        await server.register_account(message[1], message[2], message[3], addr, root)
                elif message[0] == 'quit':
                    #Quit
                    try:
                        print('client disconnected')
                        break
                    except Exception:
                        pass
                elif message[0] == 'create_folder':
                    #we can Create a folder from client to server
                    if len(message) != 2:
                        try:
                            new_msg = 'Error occured in the format of create_folder'\
                            'It must be create_folder and Folder_name'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    addr = writer.get_extra_info('peername')
                    if logined_list[addr] == 0:
                        try:
                            new_msg = 'Login to account or register an account is required primary'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        await server.create_folder(message[1], addr, root)
                elif message[0] == 'read_file':
                     #we can read the file from client to server"""
                    if len(message) != 2:
                        try:
                            new_msg = 'Error occured in the format of read_file'\
                            'It must be read_file and file_name'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    addr = writer.get_extra_info('peername')
                    if logined_list[addr] == 0:
                        try:
                            new_msg = 'Login to account or register an account is required primary'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        await server.read_file(message[1], addr, root)
                elif message[0] == 'write_file':
                    # we can Write the file from client to server
                    if len(message) <= 1:
                        try:
                            new_msg = 'Error occured in the format of write_file'\
                            'It must be write_file and file_name and data'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    addr = writer.get_extra_info('peername')
                    if logined_list[addr] == 0:
                        try:
                            new_msg = 'Login to account or register an account is required primary'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        if (len(message)) == 2:
                            string = ''
                            await server.write_file(message[1], string, addr, root)
                        elif (len(message)) > 2:
                            string = ''
                            for i in range(2, len(message)):
                                string = string + message[i] + ' '
                            await server.write_file(message[1], string, addr, root)
                        else:
                            try:
                                new_msg = 'Error occured in the format of write_file'\
                                'It must be write_file and file_name and data'
                                new_msg = new_msg.encode()
                                writer.write(new_msg + '\n'.encode())
                            except Exception:
                                pass
                elif message[0] == 'change_folder':
                    #we can replace the existing folder with new folder
                    if len(message) != 2:
                        try:
                            new_msg = 'Error occured in the format of change_folder'\
                            'It must be change_folder and name_to_be_changed'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    addr = writer.get_extra_info('peername')
                    if logined_list[addr] == 0:
                        try:
                            new_msg = 'Login to account or register an account is required primary'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        path = os.getcwd()
                        await server.change_folder(message[1], addr, path)
                elif message[0] == 'list':
                    # List is used to show existing folders from the directory
                    if len(message) != 1:
                        try:
                            new_msg = 'Error occured in the format of list of files'\
                            'it should be just list'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    addr = writer.get_extra_info('peername')
                    if logined_list[addr] == 0:
                        try:
                            new_msg = 'Login to account or register an account is required primary'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        await server.list_files(addr, root)
                elif message[0] == 'delete':
                    #Deleting the files
                    if len(message) != 3:
                        try:
                            new_msg = 'Error occured in the format of delete'\
                            'It must be delete and user_name and admin_password'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    addr = writer.get_extra_info('peername')
                    if logined_list[addr] == 0:
                        try:
                            new_msg = 'Login to account or register an account is required primary'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except Exception:
                            pass
                    else:
                        addr = writer.get_extra_info('peername')
                        await server.delete_user(message[1], message[2], addr)
                else:
                    try:
                        new_msg = 'Invalid command is entered and try again'
                        new_msg = new_msg.encode()
                        writer.write(new_msg + '\n'.encode())
                    except Exception:
                        print('Connection disconnected')
        except:
            addr = writer.get_extra_info('peername')
            # for i in range(len(client_list)):
            #     if client_list[i][3] == addr:
            #         user_name = client_list[i][0]
            #         pass_word = client_list[i][1]
            #         logined_list[(user_name,pass_word)] = 0
            logined_list[addr] = 0
            print('connection closed', addr)
            break
    writer.close()
async def main():
    host = '127.0.0.1'
    port = 8888
    ser = await asyncio.start_server(new_echo_handle, host, port)
    addr = ser.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with ser:
        await ser.serve_forever()
asyncio.run(main())
