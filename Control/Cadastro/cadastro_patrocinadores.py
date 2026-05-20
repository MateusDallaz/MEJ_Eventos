#Patrocinadores

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar
from listagem_fk import pedir_fk

def inserir_patrocinador(conexao):
    print("\n=== Cadastro de Patrocinador ===")
    nome_empresa      = input("Nome da empresa: ").strip()
    cnpj              = input("CNPJ: ").strip()
    descricao         = input("Descrição: ").strip()
    contato           = input("Contato: ").strip()
    valor_patrocinio  = input("Valor do patrocínio: ").strip()
    id_contratante    = pedir_fk(conexao, "contratante", "Contratante")
 
    sql = """
        INSERT INTO patrocinadores
            (nome_empresa, cnpj, descricao, contato,
             valor_patrocinio, id_contratante)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (nome_empresa, cnpj, descricao, contato,
              valor_patrocinio, id_contratante)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Patrocinador cadastrado com sucesso!")