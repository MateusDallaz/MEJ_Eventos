import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='mej_eventos'
    )
    print('\n=== Conexão estabelecida com sucesso! ===')
    return conexao
