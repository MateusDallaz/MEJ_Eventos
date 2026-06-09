import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar
def view_contratante_equipe(conexao):
    cursor = conexao.cursor()
    cursor.execute ('select c.nome, c.contatos, c.descricao as contratante, e.nome,e.funcao,e.contato from equipe e left join contratante c on e.id_contratante = c.id')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)
