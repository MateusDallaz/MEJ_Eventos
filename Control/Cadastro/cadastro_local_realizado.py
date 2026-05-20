#Local realizado

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar

def inserir_local(conexao):
    print("\n=== Cadastro de Local ===")
    nome_local           = input("Nome do local: ").strip()
    capacidade_total     = input("Capacidade total: ").strip()
    barracas_vendas      = input("Barracas/vendas: ").strip()
    endereco             = input("Endereço: ").strip()
    contato_responsavel  = input("Contato do responsável: ").strip()
    id_contratante       = pedir_fk(conexao, "contratante", "Contratante")
 
    sql = """
        INSERT INTO localrealizado
            (nome_local, capacidade_total, barracas_vendas,
             endereco, contato_responsavel, id_contratante)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (nome_local, capacidade_total, barracas_vendas,
              endereco, contato_responsavel, id_contratante)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Local cadastrado com sucesso!")