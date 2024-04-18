"""Filename: server.py
   Author: Xander Stephens
   This file opens the server that the players
   will connect to for the blackjack game.
   """

from socket import*
from shared import SharedCell
from client_handler import ClientHandler

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

server = socket()
server.bind(ADDRESS)
server.listen()
clients = []
game = SharedCell(clients)
while True:
    print("Waiting for connection to\n" + gethostbyname(gethostname()))
    client, address = server.accept()
    print("...connected to " + str(ADDRESS))
    handler = ClientHandler(client, game)
    clients.append(handler)
    handler.start()