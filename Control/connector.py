import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='mej_eventos'
    )
    print('\nConectado')
    return conexao
