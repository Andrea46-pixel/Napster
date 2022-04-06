#import Peer
#import CServer
from pickle import TRUE
import random
import os
import time


#per pulire la console sia se si sta utilizando linux sia windous
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#metodo per permettere all'ute di scegliere cosa vuole fare
def Apertura():
    cls()
    uscita=False
    print("Benvenuto in NapsterxSupreme\nPremere il tasto\nl per Login\nr per registrarsi\nx per uscire")
    scelta=input().lower()
    if scelta=="x":
        uscita=True
        return uscita
    if scelta=="l":
        Login()
        return uscita
    if scelta=="r":
        Registrazione()
        return uscita
    if scelta!="r" and scelta!="x" and scelta!="l":
        Apertura()

#metodo per entrare nel programma
def Login():
    cls()
    print("Inserisci la tua mail")
    mail=input()
    print("Inserisci il tuo username")
    username=input()
    print("Inserisci la tua password")
    password=input()
    CalcoloPorta()

#metodo per registrarsi nel sistema
def Registrazione():
    cls()
    print("Per tornare indietro senza completare l'operazione premi invio in tutti i campi")
    print("Inserisci il tuo username")
    username=input()
    print("Inserisci la tua mail")
    mail=input()
    print("Inserisci una password")
    password=input()
    if username and mail and password!="":
        #viene controllato che sia possibile registrarsi con i dati inseriti
        accetazione=False
        if accetazione==True:
            #collegarsi alla classe peer per fare la registrazione con l'invio dei dati al server
            print("Per entrare in NapsterxSupreme devi effetuare il Login")
            time.sleep(1)
            Login()
        else:
            print("Utente già esistente con queste credenziali")
            time.sleep(1)
            Registrazione()
    else:
        print("Hai inserito male i tuoi dati\nTi preghiamo di rinserirli correttamente\nSe vuoi tornare indietro premere x\nAltrimenti premi un qualsiasi altro tasto")
        scelta=input().lower()
        if scelta=="x":
            print("")
        else:
            Registrazione()

#metodo per generare il numero di porta con la quale il server peer si metterà in ascolto se deve condividere i file
def CalcoloPorta():
    #questo pezzo di codice serve per generare la porta sulla quale si mette dopo in ascolto il server del clien
    #viene salvata la porta in un file txt e poi aperta
    #se la porta non serve nel peer si potrebbe spostare questo pezzo direttamente nel server
    porta=random.randrange(49152, 65535)
    f=open("porta.txt", "w")
    f.write(str(porta))
    f.close()
    

def Menu(nome, mail):
    cls()
    print(f"Utente {nome}\nMail {mail}\nPremere:\nr per eseguire una ricerca\na per aggiungere un file\nd per togliere un file\nx per disconetterti")
    print("Con la ricerca successivamente sarà possibile eseguire un download")
    scelta=input().lower()
    ripeti=TRUE
    
    if scelta=="r":
        Rcerca()
        Menu(nome, mail)
        
    if scelta=="a":
        Aggiunta()
        Menu(nome, mail)
        
    if scelta=="d":
        Delete()
        Menu(nome, mail)
        
    if scelta=="x":
        ripeti=False
        print("Disconnessione da NapsterxSupreme...")
        time.sleep(1)
        
    if ripeti==True:
        Menu(nome, mail)
        
        
def Rcerca():
    Download()
    
    
def Aggiunta():
    print("")
    

def Delete():
    print("")
    
    
def Download():
    print("")


uscita = False
while uscita == False:
    cls()
    uscita=Apertura()
    if uscita==False:
        cls()
        nome=""
        mail=""
        Menu(nome,mail)
