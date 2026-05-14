import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from menu import menu
from connector import conectar

def listagem_contratante(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, endereco, data_evento, contatos FROM contratante')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)