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


def download(sid, md5, ip, porta):
    insert_query = "INSERT INTO DOWNLOAD VALUES (%s, %s, %s, %s)"
    execute_query_4par(connection, insert_query, sid, md5, ip, porta)

    n_downloads_query = "SELECT SID FROM DOWNLOAD WHERE MD5 = %s"
    n_downloads = execute_query_1par(connection, n_downloads_query, md5)
    n_downloads = str(n_downloads).zfill(5)
    answer = "ARRE"+n_downloads
    print(answer)
    return answer


pacchetto = "RREG"+"0ZQ8974GUTOH8TMC"+"4353e755883be5d0058e13e272335117"+"192.168.001.001"+"50000"
print(pacchetto[4:20])
print(pacchetto[20:52])
print(pacchetto[52:67])
print(pacchetto[67:72])
download(pacchetto[4:20], pacchetto[20:52], pacchetto[52:67], pacchetto[67:72])