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





