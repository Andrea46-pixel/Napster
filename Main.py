import Peer
import CServer
import random


porta=random.randrange(49152, 65535)

f=open("porta.txt", "w")
f.write(str(porta))
f.close()
