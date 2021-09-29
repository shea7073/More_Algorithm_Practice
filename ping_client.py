from socket import *
from time import time
from datetime import datetime

serverName = 'localhost'
serverPort = 12000

for i in range(10):
    message = "ping"
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(.5)
    now = datetime.now()
    start_time = time()
    print("PING " + str(i) + " " + str(now))
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    try:
        echo, server_address = clientSocket.recvfrom(2048)
        end_time = time()
        RTT = end_time - start_time
        print(echo.decode())
        print("Reply from ", server_address, ' RTT: ', RTT)
        print('\n')
    except timeout:
        print("Time out \n")


