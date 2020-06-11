import asyncio
import sys
class client_class:
    def __init__(self, server_ip, server_port, list, result):
        """Initilizing the variables"""
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_command_list = list
        self.result = result
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
def main():
    host = '127.0.0.1'
    port = 8888
    list = []
    result = []
    client_obj = client_class(host, port, list, result)
    asyncio.run(client_obj.client_connection())
if __name__ == "__main__":
    main()
