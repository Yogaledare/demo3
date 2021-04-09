





from socket import *


mySocket = socket(AF_INET, SOCK_DGRAM)
print(mySocket)
msg = input("enter: ")
while msg:
    mySocket.sendto(msg.encode(), ("78.71.38.26", 26000))
    msg = input("enter: ")
mySocket.close()

