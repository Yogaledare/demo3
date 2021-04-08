





from socket import *

with socket(AF_INET, SOCK_STREAM) as mySocket:
    mySocket.connect(('localhost', 12002))
    msg = input("enter: ")
    while msg:
        mySocket.send(msg.encode())
        print("received:", mySocket.recv(1024))
        msg = input("enter: ")
        # print(msg)
        # if msg:
        #     print("msg is true")
        # else:
        #     print("msg is false")


