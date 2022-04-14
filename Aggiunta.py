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

#creating a query execution function to add files
def execute_upload_query(connection, query, par1, par2, par3):
    cursor = connection.cursor(buffered = True)
    output_string =par3
    try:
        cursor.execute(query, (par1,par2,par3,))
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
    return output_string


def execute_check_query(connection, query, par1):
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


def upload(sid, md5, name):
    check_query1 = "SELECT MD5 FROM FILE WHERE MD5 = %s"
    changed1 = execute_check_query(connection, check_query1, md5)
    if changed1 ==1:
        update_query_FILE = "UPDATE FILE SET NOME = %s WHERE MD5 = %s"
        execute_query_2par(connection, update_query_FILE, name, md5)
    else:
        upload_query_FILE = "INSERT INTO FILE VALUES (%s, %s)"
        execute_query_2par(connection, upload_query_FILE, name, md5)

    check_query2 = "SELECT MD5 FROM DIRECTORY WHERE MD5 = %s AND sid=%s"
    changed2 = execute_query_2par(connection, check_query2, md5, sid)
    if changed2 ==0:
        upload_query_DIRECTORY = "INSERT INTO DIRECTORY VALUES (%s, %s)"
        execute_query_2par(connection, upload_query_DIRECTORY, sid, md5)
    

    


pacchetto = "ADDF"+"X1ZABL3QVKNJX3QL"+"4353e755883be5d0058e13e272335414"+"piratideicaraibivolumesecondoopiratideicaraibivolumesecondoopiratideicaraibivolumesecondoo12345678910"
pacchetto = pacchetto.ljust(152)
print(pacchetto)

if pacchetto[0:4] == "ADDF": 
    output = upload(pacchetto[4:20], pacchetto[20:52], pacchetto[52:153])
    #print(pacchetto[4:20])
    #print(pacchetto[20:52])
    #print(pacchetto[52:153])
else: print("Non ha richiesto l'upload")