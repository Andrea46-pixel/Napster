import socket
import os
import sys
from pathlib import Path
import time

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
        #il client-server si mette in ascolto delle richieste
        self.s.listen(10)
        while True:
            #accettazione della comunicazione
            self.conn, self.arr=self.s.accept()
            #fork per rendere il clinet concorrente
            pid=os.fork()
            if pid==0:
                print("ok")
                stringa=self.conn.recv(4).decode()
                #se la tringa iniziale è corretta avviene la comunicazione
                if stringa=="RETR":
                    md5=self.conn.recv(32).decode()
                    nomefile=""
                    #viene controllato che sia presente il file che l'utente vuole scaricare tra quelli condivisi
                    try:
                        for filename in os.listdir("filemd5"):
                            with open(os.path.join("filemd5", filename), 'r') as f:
                                text = f.read()
                                if str(text)==str(md5):
                                    nomefile=filename
                        #nome del file
                        nomefile=nomefile[:-8]

                        pachetto="AERT"
                        #controllo per verificare il nome selezionato sia un file
                        if(not Path(f'{self.percorso}/{nomefile}').is_file()):
                            self.conn.send(("AERT000000").encode())
                            return
                        else:
                            #appertura del file per la lettura
                            fd=os.open(f'{self.percorso}/{nomefile}', os.O_RDONLY)
                            #calcolo della dimensione del file per il calcolo dei chunk
                            dimensione=os.path.getsize(f'{self.percorso}/{nomefile}')
                            fc=dimensione//4096
                            resto=dimensione%4096
                            #se viene trovato del resto viene eseguito un chunk in più
                            if resto!=0:
                                fc+=1
                            #per portare a 6 la grandezza del pezzo del pacchetto vengono aggiunti gli zeri davanti
                            tmp=""
                            for i in range(0,6-len(str(fc))):
                                tmp+="0"
                            #composizione del pacchetto
                            pachetto+=str(tmp)+str(fc)

                            '''tmp+=str(fc)
                            pachetto+=tmp
                            pachetto=str(pachetto)'''

                            '''self.conn.send(pachetto.encode())
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
                            os.close(fd)'''
                            '''cont=0
                            risp=""
                            while True:
                                buf=os.read(fd,4096)
                                if not buf:
                                    break
                                cont+=1
                                risp+="0496"
                                risp+=str(buf)
                            vuoto=""
                            cont=str(cont)

                            for ii in range(len(cont),6):
                                vuoto+="0"
                            cont=str(vuoto)+str(cont)
                            mes="AERT"+cont+risp
                            self.conn.send(mes.encode())'''
                            #i 5 byte del messaggio per indicare la grandezza di un singolo chunk
                            grandezza="04096"
                            #invio pacchetto al client
                            self.conn.send(pachetto.encode())
                            #calcolo e invio dei chunk 
                            for i in range(0,fc):
                                #lettura del file
                                buf=os.read(fd,4096)
                                #invio informazioni
                                self.conn.send(grandezza.encode())
                                self.conn.send(buf)
                    #se avvengono dei problemi nella comunicazione viene impedito che si spenga tutto per un errore
                    except:
                        self.conn.send(("AERT000000").encode())
                #chiusura comunicazione con il client
                self.conn.close()

#=======================================================================================================================================
#inizializazzione del client-server
x=CServer()
#print("Server acceso")
#print(x.percorso)
#print(x.porta)
#avvio ascolto del client-server
while True:
    x.Ascolto()