import socket
import os
import sys

class CServer:

    def __init__(self):

        self.ip=""
        self.s=socket.socket()
        self.stato=True
        f=open("porta.txt", "r").read()
        self.porta=f
        print(self.porta)
        self.s.bind(("", int(self.porta)))



    def Ascolto(self):

        self.s.listen(10)
        print("Server in ascolto...")
        print(self.porta)
        while self.stato==True:
            self.conn, self.arr=self.s.accept()
            totstringa=self.conn.recv(4096).decode()
            stringa=totstringa[0:4]

            if stringa=="RETR":
                print("")
            elif stringa=="ARET":
                print("")
            elif stringa=="RREG":
                print("")



x=CServer()
print("e")
x.Ascolto()
