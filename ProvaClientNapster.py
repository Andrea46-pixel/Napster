import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 80))

pacchettoLogin = "LOGI"+"192.168.001.005"+"50000"
pacchettoAggiunta = ("ADDF"+"OR18R43EQWVCIDEX"+"4353e755883be5d0058e13e272335999"+"AggiuntaClient").ljust(152)
pacchettoRimozione = "DELF"+"OR18R43EQWVCIDEX"+"4353e755883be5d0058e13e272335999"
stringa = "Film"
stringa = stringa.ljust(20)
pacchettoRicerca = "FIND"+"5SJDAO8LE75P2P7Q"+stringa
pacchettoDownload = "RREG"+"OR18R43EQWVCIDEX"+"4353e755883be5d0058e13e272335999"+"192.168.001.001"+"50000"
pacchettoLogout = "LOGO"+"OR18R43EQWVCIDEX"

#s.send(pacchettoLogout.encode())
#print("Pacchetto inviato...")
#answer = s.recv(1024).decode()


#if pacchettoRicerca[0:4] == "FIND":
s.send(pacchettoRicerca.encode())
print("Pacchetto inviato...")
ris = s.recv(1024)
answer = pickle.loads(ris)

print(answer)
