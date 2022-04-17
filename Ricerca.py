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


def ricerca(sid, ricerca):
    query_idmd5 = "SELECT MD5,NOME FROM FILE WHERE NOME = %s"
    idmd5 = str(execute_query_1par(connection, query_idmd5, ricerca))
    
    list = []
    md5s = read_query(connection, query_idmd5, ricerca)
    #print(md5s)
    for file in md5s:
        copy_query = "SELECT MD5, SID FROM DIRECTORY WHERE MD5 = %s"
        copy = str(execute_query_1par(connection, copy_query, file[0]))
        for_ip_port = read_query(connection, copy_query, file[0])
        answer = "AFIN"+idmd5+file[0]+file[1]+copy
        #print(f"for ip port = {for_ip_port}")
        for i in for_ip_port:
            answer = "AFIN"+idmd5+file[0]+file[1]+copy
            #print(f"Questa è {i}")
            #sid_query = "SELECT SID FROM DIRECTORY WHERE MD5 = %s AND SID = %s"
            #sid = read_query_2par(connection, sid_query, i[0], i[1])
            #sid = sid[0][0]
            #ip_porta_query = "SELECT IP, PORTA FROM UTENTE WHERE SID = (SELECT SID FROM DIRECTORY WHERE MD5 = %s AND SID = %s)"
            #ip_porta = read_query_2par(connection, ip_porta_query, i[0], i[1])
            ip_porta_q = "SELECT IP, PORTA FROM UTENTE WHERE SID = %s"
            ip_port = read_query(connection, ip_porta_q, i[1])
            #print(i[1])
            #print(f"ip_port = {ip_port}")
            #answer = answer+str(ip_porta[0])+str(ip_porta[0])
            answer = answer+str(ip_port[0][0])+str(ip_port[0][1])
            list.append(answer)
            print(answer)
            
    return list
            

stringa = "Film"
stringa = stringa.ljust(100)
ricerca("5SJDAO8LE75P2P7Q", stringa)

