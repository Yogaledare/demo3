





from socket import *


mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind(('155.4.128.188', 12000))
print(gethostname())
print(mySocket)
while True:
    message, address = mySocket.recvfrom(1024)
    print("from:", address, "received:", message)
    print(type(message))
    if message.decode() == "kill":
        break
mySocket.close()

