import socket
import os
import sys
from pathlib import Path

class CServer:

    def __init__(self):

        self.ip=""

        #si collega al client 
        self.s=socket.socket()

        #si collega al server
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
                stringa=self.conn.recv(4).decode()
            
                if stringa=="RETR":
                    md5=self.conn.recv(32).decode()
                    nomefile=""
                    try:
                        for filename in os.listdir("filemd5"):
                            with open(os.path.join("filemd5", filename), 'r') as f:
                                text = f.read()
                                if str(text)==str(md5):
                                    nomefile=filename
                                    break

                        nomefile=nomefile[:-8]

                        pachetto="AERT"
                        if(not Path(f'{self.percorso}/{nomefile}').is_file()):
                            self.conn.send(("AERT").encode())
                        else:
                            fd=os.open(f'{self.percorso}/{nomefile}', os.O_RDONLY)
                            dimensione=os.path.getsize(rf'{self.percorso}/{nomefile}')
                            fc=dimensione//4096
                            resto=dimensione%4096
                            if resto!=0:
                                fc+=1

                            tmp=""
                            for i in range(0,6-len(str(fc))):
                                tmp+=0
                            tmp+=str(fc)
                            pachetto+=tmp
                            pachetto=str(pachetto)

                            self.conn.send(pachetto.encode())
                            pachetto=""

                            for i in range(0,dimensione//4096):
                                pachetto+="04096"
                                pachetto+=os.read(fd,4096).decode()
                                self.conn.send(pachetto.encode())
                                pachetto=""

                            if resto!=0:
                                tmp=""
                                for i in range(0,5-len(str(resto))):
                                    tmp+=0
                                tmp+=str(resto)
                                pachetto+=tmp
                                pachetto=str(pachetto)
                                pachetto+=os.read(fd,4096).decode()
                                self.conn.send(pachetto.encode())
                            os.close(fd)
                    except:
                        self.conn.send(("AERT000000").encode())

#=======================================================================================================================================
x=CServer()
print("Server acceso")
while True:
    x.Ascolto()
