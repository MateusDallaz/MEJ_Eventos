import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

from Lista.list_contratante import listagem_contratante

def remove_contratante(conexao):
    cursor = conexao.cursor()
    cursor.execute('DELETE * FROM {contratante} WHERE {id} = {valor}')
    conexao.commit()
