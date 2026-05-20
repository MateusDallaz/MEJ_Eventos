import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def listagem_financeiro(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT valor_evento, despesa_total, lucro_evento FROM financeiro')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)