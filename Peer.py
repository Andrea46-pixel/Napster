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