#azioni server specificate nel documento guida

#LOGIN(username, password, ip, porta)
#CERCAPEER(session id)
#AGGIUNGI(session id, md5, descrizione file)
#DELETE(session id, md5)
#RICERCA(session id, testo)
#LOGOUT(session id)
#REGISTRADOWN(md5, session id)

#porta del server 80


from socket import gethostbyname
import mysql.connector
from mysql.connector import Error
import pandas as pd
import socket


#connecting to the server
def create_server_connection(host_name, user_name, user_password, auth_plug):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            auth_plugin = auth_plug
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection




#Connecting to the Database
def create_db_connection(host_name, user_name, user_password, db_name, auth_plug):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            auth_plugin = auth_plug
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


auth_plugin = "mysql_native_password"
hostname ="localhost"
user_name = "andreaSak03"
user_password = "_FrecceOut52_"
db_name = "Napster"

create_server_connection(hostname, user_name, user_password,auth_plugin)
connection = create_db_connection(hostname, user_name, user_password, db_name, auth_plugin)

#creating a query execution function
def execute_query(connection, query):
    cursor = connection.cursor(buffered = True)
    changed = 0
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
        changed = cursor.rowcount
    except Error as err:
        print(f"Error: '{err}'")
    return changed


#populating the tables
#pop_teacher = """
#INSERT INTO UTENTE VALUES
#('andrea', 'andrea.sacchetto@iisviolamarchesini.edu.it', 'password', '192.168.1.1', '5000', TRUE),
#('jacopo', 'jacopo.corsatto@iisviolamarchesini.edu.it', 'password', '192.168.1.2', '5001', FALSE), 
#('xhoni', 'xhoni.hamzaj@iisviolamarchesini.edu.it', 'password', '192.168.1.3', '5002', TRUE),
#('nicolo', 'nicolo.risi@iisviolamarchesini.edu.it', 'password', '192.168.1.4', '5003', FALSE);
#"""

#execute_query(connection, pop_teacher)

#deleting records
#delete_user = """
#DELETE FROM UTENTE
#WHERE email='192.168.1.4';
#"""

#execute_query(connection, delete_user)


#creating a query execution function for login
def execute__login_query(connection, query, par1, par2):
    cursor = connection.cursor(buffered = True)
    changed = 0
    try:
        cursor.execute(query, (par1,par2,))
        connection.commit()
        print("Query successful")
        changed = cursor.rowcount
    except Error as err:
        print(f"Error: '{err}'")
    return changed


#function for the login
def login():
    us = input("Username: ")
    pw = input("Password: ")
    ip = socket.gethostbyname(socket.gethostname())
    print(f"Questo è l'ip: {ip}")
    porta = input("Porta: ")

    login_query = "SELECT NOME_UTENTE FROM UTENTE WHERE NOME_UTENTE = %s AND PWD = %s"

    changed = execute__login_query(connection, login_query, us, pw)

    print(f"Questo è il numero di righe modificate: {changed}")
    if changed==1:
        print("Accesso effettuato con sucecsso!\n")
        update_ip = "UPDATE UTENTE SET IP=%s WHERE NOME_UTENTE=%s"
        
        execute__login_query(connection, update_ip, ip, us)

        update_porta = "UPDATE UTENTE SET PORTA=%s WHERE NOME_UTENTE=%s"
        
        execute__login_query(connection, update_porta, porta, us)
        
    else: 
        print("Accesso negato\n")


login()


def registration():
    us = input("Username: ")
    pw = input("Password: ")
    ip = socket.gethostbyname(socket.gethostname())
    porta = "5001"
    email = input("Email: ")


    ch_us_query = "SELECT NOME_UTENTE, PWD FROM UTENTE WHERE NOME_UTENTE = {us}"
    check = execute_query(connection, ch_us_query)
    if check>0: print("Il nome utente inserito è già stato utilizzato")
    












































#import sqlite3
#from sqlite3 import Error

#def create_connection(path):
#    connection = None
#    try:
#        connection = sqlite3.connect(path)
#        print("Connection to SQLite DB successful")
#    except Error as e:
#        print(f"The error '{e}' occurred")

#    return connection
  
  
#connection = create_connection("E:\\sm_app.sqlite")





