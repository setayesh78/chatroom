#!/usr/bin/python3
import socket
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 1234
print('Waiting for connection')
server.connect((ip_address, port))
while True:
    sockets_list = [sys.stdin, server]
    read_sockets, _ , _ = select.select(sockets_list, [], [])
    
    
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message.decode('ascii'))
        else:
            message = sys.stdin.readline()
            server.send(message.encode('ascii'))
       # else:
        #    print(socks.recv(2048))

server.close()
