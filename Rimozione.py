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


pacchetto = "DELF"+"X1ZABL3QVKNJX3QL"+"4353e755883be5d0058e13e272335414"
print(pacchetto)

if pacchetto[0:4] == "DELF": 
    output = remove(pacchetto[4:20], pacchetto[20:52])
    print(output)
else: print("Non ha richiesto la rimozione")

                

