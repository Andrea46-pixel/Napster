import socket
import os
import sys

class CServer:

    def __init__(self):

        self.ip=""

        self.s=socket.socket()
        self.ss=socket.socket()

        #self.stato=True
        f=open("porta.txt", "r").read()
        self.porta=int(f)
        
        self.s.bind(("", int(self.porta)))
        
        ff=open("percorso.txt", "r").read()
        self.percorso=ff

        #self.s.bind((self.ip,self.porta))


    #verificare che abbia senso
    def Ascolto(self):
        self.s.listen(10)
        while True:
            self.conn, self.arr=self.s.accept()
            pid=os.fork()
            if pid==0:
                totstringa=self.conn.recv(4096).decode()
                stringa=totstringa[0:4]
            
                if stringa=="RETR":
                    
                    #controllare
                    #i cunk vanno calcolati, non si invia 
                    st=totstringa[5:36]
                    f=open(self.percorso+st, os.O_RDONLY)
                    while True:
                        buf=os.read(f,4096)
                        if not buf:
                            break
                        #controllare
                        self.conn.send((f"ARET").encode())
            
                elif stringa=="ARET":
                    print("")
            
                elif stringa=="RREG":
                    print("")



x=CServer()
print("Server acceso")
while True:
    x.Ascolto()
