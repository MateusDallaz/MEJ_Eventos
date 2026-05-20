#Artista

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar


def inserir_artista(conexao):
    print("\n=== Cadastro de Artista ===")
    nome         = input("Nome: ").strip()
    cnpj         = input("CNPJ: ").strip()
    contatos     = input("Contatos: ").strip()
    endereco     = input("Endereço: ").strip()
    descricao    = input("Descrição: ").strip()
    preferencias = input("Preferências: ").strip()
 
    sql = """
        INSERT INTO artista
            (nome, cnpj, contatos, endereco, descricao, preferencias)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (nome, cnpj, contatos, endereco, descricao, preferencias)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Artista cadastrado com sucesso!")