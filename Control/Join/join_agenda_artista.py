import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def join_agendaArtista(conexao):
    cursor = conexao.cursor ()
    cursor.execute("select a.nome, a.contatos, a.preferencias, a.descricao as artista, agen.data_evento, agen.nome_evento from agenda agen inner join artista a on agen.id_artista = a.id;")
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)  





   