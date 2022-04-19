import random
import os
import socket
import os.path
import time
import hashlib
import sys
import subprocess
from threading import Thread



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
        self.percorsodownload=""

        self.portacollegamento=""
        self.ipcollegamento=""
        self.nomefilecollegamento=""
        self.md5collegamento=""

#=======================================================================================================================================================================
# Logut
    def Login(self):
        cls()
        porta=80
        #self.Calcoloporta()

        hostname = socket.gethostname()
        self.ip = socket.gethostbyname(socket.gethostname()) 
        print(self.ip)
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
        
        
        #self.s.connect((self.ipserver,porta))
        self.s.connect(("localhost",80))
        
        #self.s.send((f"LOGI{self.ip}{self.porta}").encode())
        self.s.send("LOGI".encode())

        self.s.send(self.ip.encode())

        self.s.send(str(self.porta).encode())
        
        #st=self.s.recv(4096).decode()
        st=self.s.recv(20)
        self.id=st[5:16]

        self.s.close()
    
#=======================================================================================================================================================================
# per eseguire una ricerca di un possibile file da scaricare
    def Ricerca(self):
        cls()
        #sistemare
        print("Inserisci il nome del file da cercare\nCon estensione se possibile")
        self.nomefile=input()
        
        vuoto=""
        for i in range(len(self.nomefile),20):
            vuoto+=" "
        
        #self.s.send(("FIND"+str(self.id)+str(self.nomefile)+vuoto).encode())
        self.s.send("FIND".encode())
        self.s.send(self.id.encode())
        self.s.send(self.nomefile.encode())
        
        #fare in modo di vedere le iterazioni
        st=self.s.recv(4096).decode()

        x=8
        y=int(st[5:7])
        for ii in range(0,y,1):
            print(f"md5 del file {st[x:x+32]} nome file {st[x+33:x+132]} copie presenti {st[x+133:x+135]} indirizzo ip {st[x+136:x+150]} porta {st[x+151:x+156]}") 
            x+=157
        
        qw=False
        while qw==False:
            print("Premere x se non si vuole scaricare un file")
            print("premere s se si vuole scaricare un file")
            sc=input()
            if sc=="x":
                qw=True
            if sc=="s":
                qw=True
        if sc=="s":
            print("Inserisci i dati relativi ad un utente\nNon mischiare i dati")
            print("Inserisci l'indirizzo ip del proprietario del file che vuoi scaricare")
            self.ipcollegamento=input()
            print("Inserisci la porta di collegamento")
            self.portacollegamento=input()
            print("Inserisci in nome del file che vuoi scaricare")
            self.nomefilecollegamento=input()
            print("Inserisci md5 del file che vuoi scaricare")
            self.md5collegamento=input()
            self.Download()

#=======================================================================================================================================================================
# per il scaaricamento del file dal peer 
    def Download(self):
        #decidere se metterlo nel qui o nel server del client o un file avviato quando serve
        try:
            self.ss.connect((self.ipcollegamento,self.portacollegamento))
            
            fd=os.open(self.percorsodownload+self.nomefile, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o777)
            
            self.ss.send((f"RETR{self.md5collegamento}").encode())
            self.ss.recv(4).decode()
            chunkk=self.ss.recv(6).decode()
            chunkk=int(chunkk)
            
            if chunkk==0:
                print("Non è possibile scaricare il file")
                return
            
            for i in range(0,chunkk):
                buf=self.ss.recv(int(self.ss.recv(5).decode()))
                os.write(fd,buf)

            print(f"{self.nomefile} è stato scaricato correttamente")
            self.ss.close()

            self.s.connect((self.ipserver,80))
            self.s.send("RREG".encode())
            self.s.send(self.id.encode())
            self.s.send(self.md5collegamento.encode())
            self.s.send(self.ipcollegamento.encode())
            self.s.send(self.portacollegamento.encode())
            self.s.recv(1024)
        except:
            print(f"{self.nomefile} non è stato scaricato\nCi sono stati dei problemi")

#=======================================================================================================================================================================
# aggiunge un file alla lista dei file condivisi nella rete
    def Aggiungi(self):
        cls()
        print("Inserisci il nome del file che vuoi aggiungere alla condivisione\\nInserire anche l'estensione")
        #possibile miglioria
        #print("Il file deve essere presente nella cartella dove è presente questo file")
        #^^
        self.nomefile=input()
        try:
            self.Md5()

            #self.s.send(("ADDF"+str(self.id)+self.md5+self.nomefile).encode())
            self.s.send("ADDF".encode())
            self.s.send(self.id.encode())
            self.s.send(self.md5.encode())
            self.s.send(self.nomefile.encode())
            
            st=self.s.recv(4096).decode()
            #per i test
            print(f"Sono presenti {st[4:6]}")
            time.sleep(1)
            #^^
        except:
            print("File non trovato")

#=======================================================================================================================================================================
# cancellazione di un file dalla condivisione
    def Delete(self):
        cls()
        print("Quale file vuoi togliere??\nInserisci il nome")
        nome=input()

        #if os.path.exists(f"{nome}-md5.txt")==True:
        if os.path.exists(f"filemd5/{nome}-md5.txt")==True:
            #f=open(f"{nome}-md5.txt","r")
            f=open(f"filemd5/{nome}-md5.txt","r")
            
            #self.s.send((f"DELF{self.id}{str(f)}").encode())
            self.s.send("DELF".encode())
            self.s.send(self.id.encode())
            self.s.send(str(f).encode())

            self.s.recv(4096).decode()
            print("file rimosso")
        else:
            print("File non presente\nNon è stato possibile rimuovere alcun file")

#=======================================================================================================================================================================
# Logut    
    def Logout(self):
        cls()
        #self.s.send(("LOGO"+str(self.id)).encode())
        self.s.send("LOGO".encode())
        self.s.send(self.id.encode())
        st=self.s.recv(4096).decode()
        print(f"Disconnessione eseguita con successo\nAvevi condiviso {st[4:6]} file")

#=======================================================================================================================================================================
# calcolo del md5 del file
    def Md5(self):
        #sistemare l'appertira aggiungendo il percorso
        f=open(self.percorso+str(self.nomefile), "rb")
        buffer=f.read()
        self.md5=hashlib.md5(buffer).hexdigest()
        
        f=open(f"filemd5/{self.nomefile}-md5.txt","w")
        #f=open(f"{self.nomefile}-md5.txt","w")

        f.write(str(self.md5))
        f.close()
        time.sleep(1)

#=======================================================================================================================================================================
# generazione della porta che verrà utilizata per l'ascolto
    def Calcoloporta(self):
        self.porta=random.randrange(49152, 65535)
        f=open("porta.txt", "w")
        f.write(str(self.porta))
        f.close()
        #questo pezzo di codice serve per generare la porta sulla quale si mette dopo in ascolto il server del clien
        #viene salvata la porta in un file txt e poi aperta
        #se la porta non serve nel peer si potrebbe spostare questo pezzo direttamente nel server

#=======================================================================================================================================================================
# percorso dove sono presenti i file 
    def Cartella(self):
        cls()
        #si inserisce il percorso dove si trova la cartella dei file che verranno condivisi
        print("Inserisci il percorso della cartella dove sono presenti i file da condividere")
        self.percorso=input()
        f=open("percorso.txt","w")
        f.write(str(self.percorso))
        f.close()

        print("Inserisci il percorso della cartella dove vuoi scaricare i file")
        self.percorsodownload=input()


peer=Peer()

if os.path.exists('filemd5')==False:
    os.mkdir("filemd5")

peer.Calcoloporta()

peer.Login()

if peer.id=="0000000000000000":
    print("Si è verificato un problema")
    sys.exit()

peer.Cartella()

p=os.fork()
if p==0:
    uscita=False
    while uscita==False:
        cls()
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
            
            print("Premere Ctrl + C cortesemente")
            sys.exit()
            #os._exit(os.EX_OK)
else:
    #va chiamato con un tread 
    #se eseguito così si sovrappone a questo
    #subprocess.run(["python3","CServer.py"])
    #servert=Thread(subprocess.run(["python3","CServer.py"]))
    #pro=subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
    servert=Thread(subprocess.run(["python3","ps.py"]))
    servert.start()
