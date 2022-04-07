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