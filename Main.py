import Peer
import CServer
import random

#questo pezzo di codice serve per generare la porta sulla quale si mette dopo in ascolto il server del clien
#viene salvata la porta in un file txt e poi aperta
#se la porta non serve nel peer si potrebbe spostare questo pezzo direttamente nel server
porta=random.randrange(49152, 65535)
f=open("porta.txt", "w")
f.write(str(porta))
f.close()
