import asyncio
import sys
class client_class:
    """creating client class"""
    def __init__(self, server_ip, server_port, list, result):
        """Initilizing the variables"""
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_command_list = list
        self.result = result
    async def input_data(self, message, writer):
        message = message.encode()
        try:
            writer.write(message)
        except IOError:
            print('Input error')
        message = message.decode()
        message = message.split()
        if message[0] == 'login':
            """we have to login here"""
            if len(message) == 3:
                tuple = ('command :', message[0])
                nw_tuple = ('input_user_name : ', message[1])
                nw_tuple1 = ('input_password : ', message[2])
                prs_tuple = (tuple, nw_tuple, nw_tuple1)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'register':
            """register here"""
            if len(message) == 4:
                tuple = ('command :', message[0])
                nw_tuple = ('input_user_name : ', message[1])
                nw_tuple1 = ('input_password : ', message[2])
                nw_tuple2 = ('input_previllages :', message[3])
                prs_tuple = (tuple, nw_tuple, nw_tuple1, nw_tuple2)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'create_folder':
            """creating folder"""
            if len(message) == 2:
                tuple = ('command :', message[0])
                nw_tuple = ('input_folder_name : ', message[1])
                prs_tuple = (tuple, nw_tuple)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'read_file':
            """reading file"""
            if(len(message) != 2):
                tuple = ('command :', message[0])
                nw_tuple = ('input_read_name : ', message[1])
                prs_tuple = (tuple, nw_tuple)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'write_file':
            """writing the file"""
            if(len(message) == 3):
                tuple = ('command :', message[0])
                nw_tuple = ('input_write_file_name : ', message[1])
                nw_tuple1 = ('written_data : ', message[2])
                prs_tuple = (tuple, nw_tuple, nw_tuple1)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'change_folder':
            """Changing the directory"""
            if (len(message) == 2):
                tuple = ('command :', message[0])
                nw_tuple = ('folder_name : ', message[1])
                prs_tuple = (tuple, nw_tuple)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'list':
            """list is used to know whether which files are there in directory"""
            if (len(message) != 1):
                tuple = ('command :', message[0])
                prs_tuple = (tuple, nw_tuple)
                self.client_command_list.append(prs_tuple)
        elif message[0] == 'delete':
            """deleting the files"""
            if(len(message) == 3):
                tuple = ('command :', message[0])
                nw_tuple = ('input_user_name : ', message[1])
                nw_tuple1 = ('input_password : ', message[2])
                prs_tuple = (tuple, nw_tuple, nw_tuple1)
                self.client_command_list.append(prs_tuple)
        else:
            message = ' '.join(message)
            self.client_command_list.append(message)
    def commands_issued(self):
        """commands issued to the directory"""
        for i in range(len(self.client_command_list)):
            print(self.client_command_list)
    def commands_clear(self):
        """commands clear in the directory"""
        self.client_command_list = []
        message = 'commands cleared'
        self.result.append(message)
    def logout(self):
        """Logout"""
        message = 'logout successfully done'
        self.result.append(message)
    async def read_data(self, reader):
        try:
            data = await reader.read(1000)
            if len(data) != 0:
                data = data.decode()
                print(data)
        except IOError:
            print('Reading Error')
    async def client_connection(self):
        reader, writer = await asyncio.open_connection(self.server_ip, self.server_port)
        while True:
            message = input()
            if message == 'commands':
                print('1. LOGIN COMMAND')
                print('TO LOGIN YOUR ACCOUNT AND START WORK')
                print('EXPECTED_INPUT :: login user_name password')
                print('EXAMPLE :: login ramesh ramesh123')
                print('SUCCESSFUL OR UNSUCCESSFUL')
                print('UNSUCCESSFUL :: TRY AGAIN WITH CORRECT USERNAME AND PASSWORD')
                print('2. REGISTER COMMAND')
                print('TO CREATE NEW ACCOUNT')
                print('EXPECTED_INPUT :: register user_name password (admin or user)')
                print('3: CHANGE_FOLDER COMMAND')
                print('TO CAHNGE THE CURRENT_WORKING_DIRECTORY TO SPRECIFIED FOLDER ')
                print('EXPECTED_INPUT :: change_folder change_folder_name')
                print('EXAMPLE :: change_folder pictures')
                print('4. LIST COMMAND')
                print('TO PRESENT THE LIST OF FILES IN THE CURRENT_WORKING_DIRECTORY')
                print('EXPECTED_INPUT :: list')
                print('EXAMPLE :: list')
                print('5. READ_FILE COMMAND')
                print('TO READ THE DATA IN THE FILE')
                print('EXPECTED_INPUT :: read_file read_file_name')
                print('EXAMPLE :: read_file sample.txt')
                print('6. WRITE_FILE_COMMAND')
                print('TO UPDATE OR CREATE A FILE')
                print('EXPECTED_INPUT :: write_file write_file_name data_to_upadate')
                print('EXAMPLE :: write_file sample.txt hello')
                print('7. CREATE_FOLDER')
                print('TO CREATE A NEW FOLDER IN THE CURRENT_WORKING_DIRECTORY')
                print('EXPECTED_INPUT :: create_folder create_folder_name')
                print('EXAMPLE :: create_folder Ramesh')
                print('8. DELETE COMMAND')
                print('TO DELETE THE USER FROM THE SERVER')
                print('EXPECTED_INPUT :: delete user_name_to_delete admin_password')
                print('EXAMPLE :: delete ramesh ramesh1234')
            elif message == 'logout':
                self.logout()
                sys.exit()
            elif message == 'commands issued':
                self.commands_issued()
            elif message == 'commands clear':
                self.commands_clear()
            elif len(message) != 0:
                data = await self.input_data(message, writer)
            try:
                if message != 'commands' and message != 'commands clear' and message != 'commands issued':
                    data = await self.read_data(reader)
            except:
                continue                       
def main():
    host = '127.0.0.1'
    port = 8888
    list = []
    result = []
    client_obj = client_class(host, port, list, result)
    asyncio.run(client_obj.client_connection())
if __name__ == "__main__":
    main()
