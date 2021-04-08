





from socket import *

with socket(AF_INET, SOCK_STREAM) as mySocket:
    mySocket.bind(('localhost', 12002))
    mySocket.listen()
    serverON = True
    while serverON:
        connection, address = mySocket.accept()
        print("connection started with", address)
        with connection:
            message = connection.recv(1024)
            while message != b'' and message != b'\n':

                print("from: ", address, "received: ", message)

                connection.send(message)

                try:
                    msg = message.decode()
                except:
                    break

                if msg == "kill" or msg == "kill\n" or msg == "kill\r\n":
                    serverON = False
                    break
                message = connection.recv(1024)

        print("connection ended with", address)
