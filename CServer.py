import socket
import os
import sys
import Peer

class Server:

    def __init__(self, porta):
        self.ip=""
        self.porta=porta
        self.s=socket.socket()
        self.s.bind((self.ip, self.porta))
        self.stato=True



    def __Ascolto__(self):

        self.s.listen(10)
        print("Server in ascolto...")
        while self.stato==True:
            print("")




