import cmd
import random
import os
import socket
import os.path
import time
import hashlib
import sys
#import CServer
import subprocess


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def CalcoloPorta():
    #questo pezzo di codice serve per generare la porta sulla quale si mette dopo in ascolto il server del clien
    #viene salvata la porta in un file txt e poi aperta
    #se la porta non serve nel peer si potrebbe spostare questo pezzo direttamente nel server
    porta=random.randrange(49152, 65535)
    f=open("porta.txt", "w")
    f.write(str(porta))
    f.close()

class Peer:

    def __init__(self):
        self.porta=""
        self.ip=""
        self.id=""
        self.md5=""
        self.nomefile=""
        self.s=socket.socket()


    def Login(self):
        porta=80
        self.Calcoloporta()
        #hostname = socket.gethostname()
        self.ip = socket.gethostbyname(socket.gethostname()) 

        self.s.connect(("25.14.181.181",porta))

        self.s.send(("LOGI"+self.ip+self.porta).encode())
        st=self.s.recv(4096).decode()
        self.id=st[4:15]
    

    def Ricerca(self):
        
        cls()
        
        #sistemare
        print("Inserisci il nome del file da cercare\nCon estensione se possibile")
        self.nomefile=input()
        self.s.send(("FIND"+str(self.id)+str(self.nomefile)).encode())
        #fare in modo di vedere le iterazioni
        st=self.s.recv(4096).decode()

    def Download():
        #decidere se metterlo nel qui o nel server del client o un file avviato quando serve
        print("")

    def Aggiungi(self):
        
        cls()
        
        print("Inserisci il nome del file che vuoi aggiungere alla condivisione\\nInserire anche l'estensione")
        #possibile miglioria
        print("Il file deve essere presente nella cartella dove è presente questo file")
        #^^
        self.nomefile=input()
        try:
            self.Md5()
            self.s.send(("ADDF"+str(self.id)+self.md5+self.nomefile).encode())
            st=self.s.recv(4096).decode()
            #per i test
            print(f"Sono presenti {st[4:6]}")
            time.sleep(1)
            #^^
        except:
            print("File non trovato")

        
        

    def Delete(self):
        
        cls()
        
        print("Quale file vuoi togliere??\nInserisci il nome")
    
    def Logout(self):
        
        cls()
        
        self.s.send(("LOGO"+str(self.id)).encode())
        st=self.s.recv(4096).decode()
        print(f"Disconnessione eseguita con successo\nAvevi condiviso {st[4:6]}")

    def Md5(self):
        f=open(str(self.nomefile), "rb")
        buffer=f.read()
        self.md5=hashlib.md5(buffer).hexdigest()
        
        #per i test
        print(self.md5)
        time.sleep(1)

    
    def Calcoloporta(self):
        self.porta=random.randrange(49152, 65535)
        f=open("porta.txt", "w")
        f.write(str(self.porta))
        f.close()
        #questo pezzo di codice serve per generare la porta sulla quale si mette dopo in ascolto il server del clien
        #viene salvata la porta in un file txt e poi aperta
        #se la porta non serve nel peer si potrebbe spostare questo pezzo direttamente nel server
    


peer=Peer()
peer.Calcoloporta()
#peer.Login()
#va chiamato con un tread 
#se eseguito così si sovrappone a questo
subprocess.run(["python3","CServer.py"])
uscita=False
while uscita==False:
    #cls()
    print(f"Sessione {peer.id}")
    print("Digitare:\nR per cercare un file\nA per aggiungere un file\nT per togliere un file dalla condivisione\nX per disconettersi")
    scelta=input().upper()
    if scelta=="R":
        peer.Ricerca()
    elif scelta=="A":
        peer.Aggiungi()
    elif scelta=="T":
        peer.Delete()
    elif scelta=="X":
        peer.Logout()
        uscita=True
