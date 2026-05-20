import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def listagem_equipe(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, funcao, observacao FROM equipe')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)