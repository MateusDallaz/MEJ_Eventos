import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def inserir_contratante(conexao):
    nome = input("Nome: ")
    cnpj = input("CNPJ: ")
    contatos = input("Contatos: ")
    endereco = input("Endereço: ")
    descricao = input("Descrição: ")
    data_evento = input("Data do evento (AAAA-MM-DD): ") or None
    sql = """INSERT INTO contratante 
             (nome, cnpj, contatos, endereco, descricao, data_evento)
             VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (nome, cnpj, contatos, endereco, descricao, data_evento)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Registro inserido com sucesso!")