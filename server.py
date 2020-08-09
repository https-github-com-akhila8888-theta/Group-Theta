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
async def main():
    host = '127.0.0.1'
    port = 8888
    ser = await asyncio.start_server(new_echo_handle, host, port)
    addr = ser.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with ser:
        await ser.serve_forever()
asyncio.run(main())
