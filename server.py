#!/usr/bin/python3
import socket
import threading
from thread import *


def broadcast(msg):
    for client in list_of_clients:
        client.send(msg) 



def thread(connection):
    str = "Welcome to this chatroom!" 
    connection.send(str.encode('ascii'))
    list_of_clients.add(connection)
    while True:
        msg = connection.recv(2048)
        print(msg.decode('ascii'))
        broadcast(msg)
           


list_of_clients = set()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = "127.0.0.1"
port = 1234
server.bind((ip_address, port))
print("socket started", port)
server.listen(100)
print("socket is listening")
while True:
    conn, addr = server.accept()
    message = 'you are connected to server'
    conn.send(message.encode('ascii'))
    start_new_thread(thread , (conn , ))

conn.close()

server.close()
