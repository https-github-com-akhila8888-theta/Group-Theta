import asyncio
import sys
class client_class:
    def __init__(self, server_ip, server_port, list, result):
        """Initilizing the variables"""
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_command_list = list
        self.result = result
def main():
    host = '127.0.0.1'
    port = 8888
    list = []
    result = []
    client_obj = client_class(host, port, list, result)
    asyncio.run(client_obj.client_connection())
if __name__ == "__main__":
    main()
