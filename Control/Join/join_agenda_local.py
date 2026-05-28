import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def join_agenda_local(conexao):
    cursor = conexao.cursor ()
    cursor.execute("select l.nome_local, l.capacidade_total,l.endereco as local_realizado, a.data_evento, a.nome_evento, a.descricao FROM agenda a INNER JOIN local_realizado l ON a.id_local = l.id")
    resultado = cursor.fetchall()
    for i in resultado:
        print(i) 
        