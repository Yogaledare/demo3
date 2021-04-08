





from socket import *


mySocket = socket(AF_INET, SOCK_DGRAM)
msg = input("enter: ")
while msg:
    mySocket.sendto(msg.encode(), ("129.16.29.51", 12000))
    msg = input("enter: ")
