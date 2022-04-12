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
from threading import Thread
import signal


#opzioni per miglioramenti
#creare una cartella per i file md5

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


class Peer:


    def __init__(self):
        
        self.porta=""
        self.ip=""
        self.id=""
        
        self.md5=""
        self.nomefile=""
        
        self.ipserver=""
        self.s=socket.socket()
        self.ss=socket.socket()
        
        self.percorso=""
        #self.md5f=[]
        #self.md5n=[]

        self.portacollegamento=""
        self.ipcollegamento=""


    def Login(self):
        cls()
        porta=80
        self.Calcoloporta()
        #hostname = socket.gethostname()
        #self.ip = socket.gethostbyname(socket.gethostname()) 
        ok=False
        while ok==False:
            print("Inserisci il tuo indirizzo ip\nMetti gli zeri se il numero non composto da 3 cifre")
            self.ip=input()
            if self.ip.__len__()==15:
                ok=True
            else:
                print("Hai inseriti male il tuo ip")   
        ok=False
        while ok==False:
            print("Inserisci l'indirizzo ip del server\nMetti gli zeri se il numero non composto da 3 cifre")
            self.ipserver=input()
            if self.ipserver.__len__()==15:
                ok=True
            else:
                print("Hai inseriti male il l'indirizzo del server")
        self.s.connect((self.ipserver,porta))
        self.s.send((f"LOGI{self.ip}{self.porta}").encode())
        st=self.s.recv(4096).decode()
        #controllare
        self.id=st[5:16]
    

    def Ricerca(self):
        cls()
        #sistemare
        print("Inserisci il nome del file da cercare\nCon estensione se possibile")
        self.nomefile=input()
        self.s.send(("FIND"+str(self.id)+str(self.nomefile)).encode())
        #fare in modo di vedere le iterazioni
        st=self.s.recv(4096).decode()


    def Download(self):
        #decidere se metterlo nel qui o nel server del client o un file avviato quando serve
        try:
            self.ss.connect((self.ipcollegamento,self.portacollegamento))
            fd=os.open(self.nomefile, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o777)
            while True:
                buf=self.ss.recv(4096)
                if not buf:
                    break
                os.write(fd,buf)
            print(f"{self.nomefile} è stato scaricato correttamente")
        except:
            print(f"{self.nomefile} non è stato scaricato\nCi sono stati dei problemi")


    def Aggiungi(self):
        cls()
        print("Inserisci il nome del file che vuoi aggiungere alla condivisione\\nInserire anche l'estensione")
        #possibile miglioria
        #print("Il file deve essere presente nella cartella dove è presente questo file")
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
        nome=input()
        if os.path.exists(f"{nome}-md5.txt")==True:
            f=open(f"{nome}-md5.txt","r")
            self.s.send((f"DELF{self.id}{str(f)}").encode())
            self.s.recv(4096).decode()
            print("file rimosso")
        else:
            print("File non presente\nNon è stato possibile rimuovere alcun file")

    
    def Logout(self):
        cls()
        self.s.send(("LOGO"+str(self.id)).encode())
        st=self.s.recv(4096).decode()
        print(f"Disconnessione eseguita con successo\nAvevi condiviso {st[4:6]} file")


    def Md5(self):
        #sistemare l'appertira aggiungendo il percorso
        f=open(str(self.nomefile), "rb")
        buffer=f.read()
        self.md5=hashlib.md5(buffer).hexdigest()
        #per i test
        print(self.md5)
        #^^
        f=open(f"{self.nomefile}-md5.txt","w")
        f.write(str(self.md5))
        f.close()
        time.sleep(1)

    
    def Calcoloporta(self):
        self.porta=random.randrange(49152, 65535)
        f=open("porta.txt", "w")
        f.write(str(self.porta))
        f.close()
        #questo pezzo di codice serve per generare la porta sulla quale si mette dopo in ascolto il server del clien
        #viene salvata la porta in un file txt e poi aperta
        #se la porta non serve nel peer si potrebbe spostare questo pezzo direttamente nel server


    def Cartella(self):
        cls()
        #si inserisce il percorso dove si trova la cartella dei file che verranno condivisi
        print("Inserisci il percorso della cartella dove sono presenti i file da condividere")
        self.percorso=input()
        f=open("percorso.txt","w")
        f.write(str(self.percorso))
        f.close()


peer=Peer()

if os.path.exists('filemd5')==False:
    os.mkdir("filemd5")

peer.Calcoloporta()

peer.Login()

servert=0

peer.Cartella()

p=os.fork()
if p==0:
    uscita=False
    while uscita==False:
        #cls()
        print(f"Sessione {peer.id}")
        print(f"Percorso cartella {peer.percorso}")
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
            #os.close(servert)
            uscita=True
            #os.killpg(os.getpid(pro.pid), signal.SIGTERM)
            sys.exit()
            #os._exit(os.EX_OK)
else:
    #va chiamato con un tread 
    #se eseguito così si sovrappone a questo
    #subprocess.run(["python3","CServer.py"])
    #servert=Thread(subprocess.run(["python3","CServer.py"]))
    #pro=subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
    servert=Thread(subprocess.run(["python3","cs2.py"]))
    servert.start()
