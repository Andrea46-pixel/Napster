#from importlib.util import set_loader
import socket
import os
import hashlib
import sys
#import CServer
#import Main
import time

#azioni peer specificate nel documento guido

#Il singolo peer possiederà in locale:
#il proprio session id, che indica la coppia ip-porta in ascolto
#una lista contenente il percorso del file in condivisione e il rispettivo md5

#Metodi:
#SEND(md5)
#CALCOLAMD5(percorso del file)
#LOGIN(ip, porta)
#AGGIUNGI(session id, file md5, descrizione del file)
#DELETE(session id, md5)
#RICERCA(session id,testo)
#RECEIVE(md5, ip, port)
#LOGOUT(session id)
#REGISTRAZIONE

class Peer:

    

    def __init__(self):
        self.porta=0
        self.ip=""
        self.nome_utente=""
        self.mail=""
        self.password=""
        self.server=socket.socket()
        #self.client=socket.socket()
        #self.__Connessione__()
        
    #passare mail e password
    def __Login__(self, mail, user, passw):
        f=open("porta.txt", "r").read()
        self.porta=int(f)
        #self.server.connect(("25.14.181.181",5000))
        self.server.send((f"{mail}.{user}.{passw}").encode())
        x=self.server.recv(4096)
        print(x)
        time.sleep(2)
        self.server.close()





    def __Registrazione__(self, nome_utente, mail, password):
        self.server.connect((self.ip,80))
        


    #passare il nome del file
    def __Aggiungi__(self):
        print("")

    def __Delete__(self):
        print("")
    
    def __Ricerca__(self):
        print("")

    def __Logout__(self):
        self.s.close()

    def __Recive__(self):
        print("")

    def __CalcoloMd5__(self):
        print("")

    def __Connessione__(self):

        #self.ip=socket.gethostbyname(socket.gethostname())

        #connessione con il server centrale
        self.server.connect(("25.14.181.181",5000))
        #invio messaggio di aggiornamento stato server
        #self.server.send(f"LOGI".encode)
