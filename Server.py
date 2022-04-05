#azioni server specificate nel documento guida

#LOGIN(ip, porta)
#CERCAPEER(session id)
#AGGIUNGI(session id, md5, descrizione file)
#DELETE(session id, md5)
#RICERCA(session id, testo)
#LOGOUT(session id)
#REGISTRADOWN(md5, session id)

#porta del server 80

import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
  
  
connection = create_connection("E:\\sm_app.sqlite")

#da installare
#$ pip install mysql-connector-python




