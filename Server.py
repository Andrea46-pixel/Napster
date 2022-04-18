#porta del server 80

import mysql.connector
from mysql.connector import Error
import socket
import random
import string
import os
import pickle


#connecting to the server
#def create_server_connection(host_name, user_name, user_password, auth_plug):
#    connection = None
#    try:
#        connection = mysql.connector.connect(
#            host=host_name,
#            user=user_name,
#            passwd=user_password,
#            auth_plugin = auth_plug
#        )
#        print("MySQL Database connection successful")
#    except Error as err:
#        print(f"Error: '{err}'")

#    return connection

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

#create_server_connection(hostname, user_name, user_password,auth_plugin)
#connection = create_db_connection(hostname, user_name, user_password, db_name, auth_plugin)

#creating some queries execution function
def execute_query_1par(connection, query, par1):
    cursor = connection.cursor(buffered = True)
    try:
        cursor.execute(query, (par1,))
        connection.commit()
        print("Query successful")
        changed = cursor.rowcount
    except Error as err:
        print(f"Error: '{err}'")
    return changed

def execute_query_2par(connection, query, par1,par2):
    cursor = connection.cursor(buffered = True)
    try:
        cursor.execute(query, (par1,par2,))
        connection.commit()
        print("Query successful")
        changed = cursor.rowcount
    except Error as err:
        print(f"Error: '{err}'")
    return changed

def execute_query_3par(connection, query, par1, par2, par3):
    cursor = connection.cursor(buffered = True)
    output_string =par3
    try:
        cursor.execute(query, (par1,par2,par3,))
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    return output_string

def execute_query_4par(connection, query, par1, par2, par3, par4):
    cursor = connection.cursor(buffered = True)
    output_string =par3
    try:
        cursor.execute(query, (par1,par2,par3,par4,))
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    return output_string

def read_query(connection, query,par1):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, (par1,))
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def read_query_2par(connection, query,par1,par2):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, (par1,par2,))
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


#=========================================LOGIN===================================================#

#creating a query execution function for login
#leggermente diversa da quella sopra perchè restituisce la stringa di 0 in caso di errore, ma da migliorare
#affinché posso essere usata univocamente quella precedente
def execute__login_query(connection, query, par1, par2, par3):
    cursor = connection.cursor(buffered = True)
    #changed = 0
    output_string =par3
    try:
        cursor.execute(query, (par1,par2,par3,))
        connection.commit()
        print("Query successful")
        #changed = cursor.rowcount
    except Error as err:
        output_string = "0000000000000000"  
        print(f"Error: '{err}'")
    return output_string


#function to generate a session ID
def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#function for the login action
def login(ip, porta):
    login_query = "INSERT INTO UTENTE VALUES (%s, %s, %s)"
    sid = id_generator()
    output = execute__login_query(connection, login_query, ip, porta, sid)
    answer = "ALGI"+output
    return answer



#=========================================AGGIUNTA===================================================#


def upload(sid, md5, name):
    check_query1 = "SELECT MD5 FROM FILE WHERE MD5 = %s"
    changed1 = execute_query_1par(connection, check_query1, md5)
    if changed1 ==1:
        update_query_FILE = "UPDATE FILE SET NOME = %s WHERE MD5 = %s"
        execute_query_2par(connection, update_query_FILE, name, md5)
    else:
        upload_query_FILE = "INSERT INTO FILE VALUES (%s, %s)"
        execute_query_2par(connection, upload_query_FILE, name, md5)

    check_query2 = "SELECT MD5 FROM DIRECTORY WHERE MD5 = %s AND sid=%s"
    changed2 = execute_query_2par(connection, check_query2, md5, sid)
    print(changed2)
    if changed2 ==0:
        upload_query_DIRECTORY = "INSERT INTO DIRECTORY VALUES (%s, %s)"
        execute_query_2par(connection, upload_query_DIRECTORY, sid, md5)
    
    copy_query = "SELECT MD5 FROM DIRECTORY WHERE MD5 = %s"
    copy = str(execute_query_1par(connection, copy_query, md5))
    copy = copy.zfill(3)
    answer = "AADD"+copy
    return answer


#=========================================RIMOZIONE===================================================#

def remove(sid, md5):
    check_query1 = "SELECT MD5 FROM DIRECTORY WHERE MD5=%s"
    changed1 = execute_query_1par(connection, check_query1, md5)
    if changed1==0:
        print("Il file indicato non è stato condiviso")
    else:
        check_query2 = "SELECT MD5 FROM DIRECTORY WHERE SID = %s AND MD5 = %s"
        changed2 = execute_query_2par(connection, check_query2, sid, md5)
        if changed2 ==0:
            print("Non hai ancora caricato questo file")
        else:
            checkCorrispondenza = changed1-changed2
            if checkCorrispondenza ==0:
                delete_query_file = "DELETE FROM FILE WHERE MD5 = %s"
                execute_query_1par(connection, delete_query_file, md5)
            delete_query_directory = "DELETE FROM DIRECTORY WHERE SID = %s AND MD5=%s"
            execute_query_2par(connection, delete_query_directory, sid, md5)

    check_query3 = "SELECT MD5 FROM DIRECTORY WHERE MD5 = %s"
    copy = str(execute_query_1par(connection, check_query3, md5))
    copy = copy.zfill(3)
    answer = "ADEL"+copy
    return answer



#=========================================RICERCA===================================================#

def ricerca(sid, ricerca):
    query_idmd5 = "SELECT MD5,NOME FROM FILE WHERE NOME = %s"
    idmd5 = str(execute_query_1par(connection, query_idmd5, ricerca))
    
    list = []
    md5s = read_query(connection, query_idmd5, ricerca)
    for file in md5s:
        copy_query = "SELECT MD5, SID FROM DIRECTORY WHERE MD5 = %s"
        copy = str(execute_query_1par(connection, copy_query, file[0]))
        for_ip_port = read_query(connection, copy_query, file[0])
        answer = "AFIN"+idmd5+file[0]+file[1]+copy
        for i in for_ip_port:
            answer = "AFIN"+idmd5+file[0]+file[1]+copy
            ip_porta_q = "SELECT IP, PORTA FROM UTENTE WHERE SID = %s"
            ip_port = read_query(connection, ip_porta_q, i[1])
            answer = answer+str(ip_port[0][0])+str(ip_port[0][1])
            list.append(answer)
    return list



#=========================================DOWNLOAD===================================================#

def download(sid, md5, ip, porta):
    insert_query = "INSERT INTO DOWNLOAD VALUES (%s, %s, %s, %s)"
    execute_query_4par(connection, insert_query, sid, md5, ip, porta)

    n_downloads_query = "SELECT SID FROM DOWNLOAD WHERE MD5 = %s"
    n_downloads = execute_query_1par(connection, n_downloads_query, md5)
    n_downloads = str(n_downloads).zfill(5)
    answer = "ARRE"+n_downloads
    print(answer)
    return answer




#=========================================LOGOUT===================================================#


def logout(sid):
    query_check_files = "SELECT SID FROM DIRECTORY WHERE SID = %s"
    changed1 = execute_query_1par(connection, query_check_files, sid)
    print(changed1)

    #cancellazione files dell'utente
    #for i in range(changed1):
    select_query = "SELECT MD5 FROM DIRECTORY WHERE SID =%s"
    n_files = str(execute_query_1par(connection, select_query, sid))
    print(f"n° files: {n_files}")
    files = read_query(connection, select_query, sid)
    i=0
    for file in files:
        print(f"questo è file: {file[i]}")
        check_query1 = "SELECT MD5 FROM DIRECTORY WHERE MD5 = %s"
        changed2 = execute_query_1par(connection, check_query1, file[i])
        if changed2 == 1:
            delete_query_FILE = "DELETE FROM FILE WHERE MD5 = %s"
            execute_query_1par(connection, delete_query_FILE, file[i])
        delete_query_DIRECTORY = "DELETE FROM DIRECTORY WHERE MD5 = %s AND SID = %s"
        execute_query_2par(connection, delete_query_DIRECTORY, file[i], sid)
        #i=i+1
    
    #cancellazione utente
    logout_query = "DELETE FROM UTENTE WHERE SID = %s"
    execute_query_1par(connection, logout_query, sid)
    n_files = n_files.zfill(3)
    answer = "ALGO"+n_files
    return answer


#=========================================AZIONI_SERVER===================================================#

def azione(intestazione):

    if intestazione == "LOGI":
        ip = conn.recv(15).decode()
        porta = conn.recv(5).decode()
        answer = login(ip, porta)
        conn.send(answer.encode())

    elif intestazione == "ADDF":
        sid = conn.recv(16).decode()
        md5 = conn.recv(32).decode()
        nome = conn.recv(100).decode()
        answer = upload(sid, md5, nome)
        conn.send(answer.encode())

    elif intestazione == "DELF":
        sid = conn.recv(16).decode()
        md5 = conn.recv(32).decode()
        answer = remove(sid, md5)
        conn.send(answer.encode())

    elif intestazione == "FIND":
        sid = conn.recv(16).decode()
        research = conn.recv(20).decode()
        res = research.ljust(100)
        ris = ricerca(sid, res)
        print(f"Risposta: {ris}")
        answer = pickle.dumps(ris)
        conn.send(answer)
        
    elif intestazione == "RREG":
        sid = conn.recv(16).decode()
        md5 = conn.recv(32).decode()
        ip = conn.recv(15).decode()
        porta = conn.recv(5).decode()
        answer = download(sid, md5, ip, porta)
        conn.send(answer.encode())

    elif intestazione == "LOGO":
        sid = conn.recv(16)
        answer = logout(sid)
        conn.send(answer.encode())



#=========================================CONNESSIONE===================================================#

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 80))
s.listen(40)

while True:
    print("Server in ascolto...")
    conn, addr = s.accept()
    pid = os.fork()
    if pid==0:
        connection = create_db_connection(hostname, user_name, user_password, db_name, auth_plugin)
        intestazione = conn.recv(4).decode()
        azione(intestazione)
        conn.close()
        exit()






    












































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





