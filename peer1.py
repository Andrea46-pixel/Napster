import random
import os
import socket
import os.path
import time
import hashlib
import sys
import subprocess
from threading import Thread
import pickle



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


    
    def Socket(self):
        self.s=socket.socket()
        self.s.connect((str(self.ipserver),80))

#=======================================================================================================================================================================
# Logut
    def Login(self):
        cls()

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
            print("Inserisci l'indirizzo ip del server")
            self.ipserver=input()
            if self.ipserver.__len__()>=7 and len(self.ipserver)<=15:
                ok=True
            else:
                print("Hai inseriti male il l'indirizzo del server")
        
        self.Socket()
        
        self.s.send((f"LOGI{self.ip}{self.porta}").encode())
        st=self.s.recv(20).decode()

        self.id=st[4:20]

        self.s.close()
        return
    
#=======================================================================================================================================================================
# per eseguire una ricerca di un possibile file da scaricare
    def Ricerca(self):
        cls()

        print("Inserisci il nome del file da cercare\nCon estensione se possibile")
        self.nomefile=input()
        vuoto=""
        for i in range(len(self.nomefile),20):
            vuoto+=" "
        
        self.Socket()

        st=[]
        self.s.send(("FIND"+str(self.id)+str(self.nomefile)+vuoto).encode())
        
        risp=self.s.recv(1024).decode()

        self.s.close()

        x = 7
        idmd5  = int(risp[4:7].strip())
        print(f"\nRISULTATI TROVATI: {idmd5}")
        for i in range(0,idmd5):
            md5 = risp[x:x+32]
            name = risp[x+32:x+132]
            copy = risp[x+132: x+135]
            ip = risp[x+135: x+150]
            port = risp[x+150: x+155]
            print(f"\nMD5: {md5}\nNAME: {name.strip()}\nCOPY: {copy}\nIP: {ip}\nPORT: {port}\n")
            x= x+155
            


        qw=False
        while qw==False:
            print("Premere x se non si vuole scaricare un file")
            print("premere s se si vuole scaricare un file")
            sc=input()
            if sc=="x":
                qw=True
                return
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
            print("Inserisci md5 del file che vuoi scaricare collegato al nome del file")
            self.md5collegamento=input()
            self.Download()

#=======================================================================================================================================================================
# per il scaaricamento del file dal peer 
    def Download(self):
        #decidere se metterlo nel qui o nel server del client o un file avviato quando serve
        try:
            self.ss=socket.socket()
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
            time.sleep(1)
            self.ss.close()

            self.Socket()

            self.s.send((f"RREG{self.id}{self.md5collegamento}{self.ipcollegamento}{self.portacollegamento}").encode())
            risp=self.s.recv(1024).decode()
            
            self.s.close()
        
        except:
            print(f"{self.nomefile} non è stato scaricato\nCi sono stati dei problemi")
            time.sleep(1)
            try:
                self.ss.close()
                self.s.close()
            except:
                print("")
        
        return

#=======================================================================================================================================================================
# aggiunge un file alla lista dei file condivisi nella rete
    def Aggiungi(self):
        cls()

        print("Inserisci il nome del file che vuoi aggiungere alla condivisione\\nInserire anche l'estensione")
        self.nomefile=input()

        try:
            self.Md5()

            self.Socket()
            self.s.send(("ADDF"+str(self.id)+self.md5+(self.nomefile).ljust(100)).encode())
            
            st=self.s.recv(4096).decode()

            self.s.close()
            #sistemare
            print(f"Sono presenti {st[5:7]}")
            
            time.sleep(1)

        except:
            print("File non trovato")
            try:
                self.s.close()
            except:
                print("")

        return
#=======================================================================================================================================================================
# cancellazione di un file dalla condivisione
    def Delete(self):
        cls()

        print("Quale file vuoi togliere??\nInserisci il nome")
        nome=input()

        if os.path.exists(f"filemd5/{nome}-md5.txt")==True:
            f=open(f"filemd5/{nome}-md5.txt","r").read()
            
            self.Socket()
            self.s.send((f"DELF{self.id}{str(f)}").encode())
            self.s.recv(4096).decode()
            print("file rimosso")
            time.sleep(1)
            self.s.close()
        else:
            print("File non presente\nNon è stato possibile rimuovere alcun file")
            time.sleep(1)
            try:
                self.s.close()
            except:
                print("")

        return
#=======================================================================================================================================================================
# Logut    
    def Logout(self):
        cls()

        print(self.ipserver)
        self.Socket()
        self.s.send(("LOGO"+str(self.id)).encode())

        st=self.s.recv(4096).decode()
        #sistemare
        print(f"Disconnessione eseguita con successo\nAvevi condiviso {st[5:7]} file")

        self.s.close()

#=======================================================================================================================================================================
# calcolo del md5 del file
    def Md5(self):

        f=open(f"{self.percorso}/{str(self.nomefile)}", "rb")
        buffer=f.read()
        self.md5=hashlib.md5(buffer).hexdigest()
        
        f=open(f"filemd5/{self.nomefile}-md5.txt","w")

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
    time.sleep(1)
    peer.Logout()
    sys.exit()

peer.Cartella()

p=os.fork()
if p==0:
    uscita=False
    while uscita==False:
        cls()
        print(f"Sessione {peer.id}")
        print(f"Percorso cartella file condivisi {peer.percorso}")
        print(f"Percorso cartella file scaricati {peer.percorsodownload}")
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
