#import Peer
#import CServer
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
    CalcoloPorta()

#metodo per registrarsi nel sistema
def Registrazione():
    cls()
    print("Inserisci il tuo username")
    username=input()
    print("Inserisci la tua mail")
    mail=input()
    print("Inserisci una password")
    password=input()
    if username and mail and password!="":
        #collegarsi alla classe peer per fare la registrazione con l'invio dei dati al server
        print("Per entrare in NapsterxSupreme devi effetuare il Login")
        #time.sleep(1000)
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



uscita = False
while uscita == False:
    cls()
    uscita=Apertura()
    if uscita!=False:
        cls()
        print("ciao")
