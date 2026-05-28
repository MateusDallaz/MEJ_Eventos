import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def join_contratante_marketing(conexao):
    cursor = conexao.cursor()
    cursor.execute('select c.nome, c.contatos, c.descricao as contratante, m.meio_comunicacao, m.tipo_midia, m.custo from marketing m left join contratante c on m.id_contratante = c.id')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)