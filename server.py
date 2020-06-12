import asyncio
import queue
from server_main import server_class
client_list = []
logined_list = {}
temporary_clients = {}
read_file_data = {}
queue_data = queue.Queue()
result = []
async def new_echo_handle(reader, writer):
    server = server_class(reader, writer, client_list, logined_list,\
                          temporary_clients, read_file_data, result)
    addr = writer.get_extra_info('peername')
    logined_list[addr] = 0
    message = f"{addr} is connected !!!!"
    print(message)
    while True:
        try:
            data = await reader.read(100)
            new_msg = data.decode()
            print(new_msg)
            queue_data.put(data)
            while queue_data.empty() == 0:
                queue_data.get()
                message = data.decode().split()
                if message[0] == 'login':
                    """login here"""
                    if len(message) != 3:
                        try:
                            new_msg = 'Error occured in syntax of login\
                                        data It must login user_name password'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except:
                            print('client connection disconnected')
                    else:
                        addr = writer.get_extra_info('peername')
                        await server.login_account(message[1], message[2], addr)
                elif message[0] == 'register':
                    """ before login we have to  register"""
                    if len(message) != 4:
                        try:
                            new_msg = 'Error occured in syntax of register data\
                                        It must login user_name password privilages'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except:
                            pass
                    else:
                        addr = writer.get_extra_info('peername')
                        await server.register_account(message[1], message[2], message[3], addr)
                elif message[0] == 'quit':
                    """Quit"""
                    try:
                        print('client disconnected')
                        break
                    except:
                        pass
                elif message[0] == 'create_folder':
                    """Create folder"""
                    if len(message) != 2:
                        try:
                            new_msg = 'Error occured in the format of create_folder\
                                         It must be create_folder and Folder_name'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except:
                            pass
                    else:
                        await server.create_folder(message[1])
                elif message[0] == 'read_file':
                    """ reading the file"""
                    if len(message) != 2:
                        try:
                            new_msg = 'Error occured in the format of read_file \
                                         It must be read_file and file_name'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except:
                            pass
                    else:
                        await server.read_file(message[1])
                elif message[0] == 'write_file':
                    """Writing the file"""
                    if len(message) != 3:
                        try:
                            new_msg = 'Error occured in the format of write_file\
                                         It must be write_file and file_name and data'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except:
                            pass
                    else:
                        await server.write_file(message[1], message[2])
                elif message[0] == 'change_folder':
                    """Changing the directory"""
                    if len(message) != 2:
                        try:
                            new_msg = 'Error occured in the format of change_folder\
                                         It must be change_folder and name_to_be_changed'
                            new_msg = new_msg.encode()
                            writer.write(new_msg + '\n'.encode())
                        except:
                            pass
                    else:
                        await server.change_folder(message[1])
           
        except:
            addr = writer.get_extra_info('peername')
            logined_list[addr] = 0
            print('connection closed', addr)
            break
    writer.close
async def main():
    host = '127.0.0.1'
    port = 8888
    ser = await asyncio.start_server(new_echo_handle, host, port)
    addr = ser.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with ser:
        await ser.serve_forever()
asyncio.run(main())
