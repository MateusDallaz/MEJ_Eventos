import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def listagem_agenda(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT nome_evento, data_evento, descricao FROM agenda')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)