def registration():
    us = input("Username: ")
    pw = input("Password: ")
    ip = socket.gethostbyname(socket.gethostname())
    porta = "5001"
    email = input("Email: ")


    ch_us_query = "SELECT NOME_UTENTE, PWD FROM UTENTE WHERE NOME_UTENTE = {us}"
    check = execute_query(connection, ch_us_query)
    if check>0: print("Il nome utente inserito è già stato utilizzato")