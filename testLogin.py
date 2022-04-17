import mysql.connector
from mysql.connector import Error
import socket
import random
import string

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


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def login(ip, porta):
    login_query = "INSERT INTO UTENTE VALUES (%s, %s, %s)"
    sid = id_generator()
    output = execute__login_query(connection, login_query, ip, porta, sid)
    answer = "ALGI"+output
    return answer



pacchetto = "LOGI"+"192.168.001.004"+"50000"

#ip = socket.gethostbyname(socket.gethostname())
if pacchetto[0:4] == "LOGI": 
    output = login(pacchetto[4:19], pacchetto[19:24])
    print(output)
else: print("Non ha richiesto il login")

