import mysql.connector
from mysql.connector import Error
import socket
import random

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

connection = create_db_connection(hostname, user_name, user_password, db_name, auth_plugin)

#creating a query execution function for login
def execute__login_query(connection, query, par1, par2, par3):
    cursor = connection.cursor(buffered = True)
    changed = 0
    try:
        cursor.execute(query, (par1,par2,par3,))
        connection.commit()
        print("Query successful")
        changed = cursor.rowcount
    except Error as err:
        print(f"Error: '{err}'")
    return changed


def login(ip, porta):
    login_query = "INSERT INTO UTENTE VALUES (%s, %s, %s)"
    #sid = random.randint(0,22)
    digits = 0
    sid = random.randrange(0, 9999999999999999)
    n=sid
    while(n>0):
        digits=digits+1
        n=n//10

    while digits<16:
        number_str = str(sid)
        zero_filled_number = number_str.zfill(5)
        sid = zero_filled_number
        digits=digits+1
        
    changed = execute__login_query(connection, login_query, ip, porta, sid)

    print(f"SESSION ID: {sid}")



pacchetto = "LOGI"+"192.168.001.001"+"50000"
action = pacchetto[0:4]
print(action)

if action == "LOGI":
    #porta = input("Inserisci la porta: ")
    #ip = socket.gethostbyname(socket.gethostname())
    #ip = input("Inserisci IP: ")
    login(pacchetto[4:19], pacchetto[19:24])
else:
    print("Non ha richiesto il login")

