import asyncio
import sys

def main():
    host = '127.0.0.1'
    port = 8888
    list = []
    result = []
    client_obj = client_class(host, port, list, result)
    asyncio.run(client_obj.client_connection())
if __name__ == "__main__":
    main()
