import mysql.connector
from mysql.connector import Error

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

#creating a query execution function
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


def execute_query_1par(connection, query, par1):
    cursor = connection.cursor(buffered = True)
    changed = 0
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
    changed = 0
    try:
        cursor.execute(query, (par1,par2,))
        connection.commit()
        print("Query successful")
        changed = cursor.rowcount
    except Error as err:
        print(f"Error: '{err}'")
    return changed


def read_query(connection, query,par1):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, (par1,))
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


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
        

pacchetto = "LOGO"+"X1ZABL3QVKNJX3Q2"
if pacchetto[0:4] == "LOGO": 
    output = logout(pacchetto[4:20])
    print(output)
else: print("Non ha richiesto il logout")