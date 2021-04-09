





from socket import *


mySocket = socket(AF_INET, SOCK_DGRAM)
msg = input("enter: ")
while msg:
    mySocket.sendto(msg.encode(), ("155.4.128.188", 12000))
    msg = input("enter: ")
