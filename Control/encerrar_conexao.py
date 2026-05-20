import mysql.connector
from connector import conectar

def fechar_conexao(conexao):
    conexao.close()
    print('\n=== Conexão encerrada. Até logo! ===')