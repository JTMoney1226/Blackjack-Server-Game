"""Filename: client.py
   Author: Jacob Miller
   This is the file that the players will use to connect 
   to the server.
"""

from socket import *
from codecs import decode

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)
CODE = "ascii"
BUFSIZE = 1024

server = socket()
server.connect(ADDRESS)
print(decode(server.recv(BUFSIZE), CODE))
while True:
    message = input("> ")
    if not message:
        break
    server.send(bytes(message, CODE))
    reply = decode(server.recv(BUFSIZE), CODE)
    if reply == "Waiting on server":
        print("Waiting on server")
        print(decode(server.recv(BUFSIZE), CODE))
    elif not reply:
        print("Server disconnected")
        break
    else:
        print(reply)

server.close()
