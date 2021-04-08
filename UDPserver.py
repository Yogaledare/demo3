





from socket import *

with socket(AF_INET, SOCK_DGRAM) as mySocket:
    mySocket.bind(('129.16.29.51', 12000))
    while True:
        message, address = mySocket.recvfrom(1024)
        print("from:", address, "received:", message)
        print(type(message))
        if message.decode() == "kill":
            break


