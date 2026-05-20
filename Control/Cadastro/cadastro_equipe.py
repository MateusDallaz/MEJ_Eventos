#Equipe

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar
from listagem_fk import pedir_fk


def inserir_equipe(conexao):
    print("\n=== Cadastro de Equipe ===")
    nome             = input("Nome: ").strip()
    cpf              = input("CPF: ").strip()
    funcao           = input("Função: ").strip()
    contato          = input("Contato: ").strip()
    data_contratacao = input("Data de contratação (AAAA-MM-DD): ").strip() or None
    valor_diaria     = input("Valor da diária: ").strip()
    observacao       = input("Observação: ").strip()
    id_contratante   = pedir_fk(conexao, "contratante", "Contratante")
    id_despesas      = pedir_fk(conexao, "despesas",    "Despesa", ("id", "custo_contratacao"))
 
    sql = """
        INSERT INTO equipe
            (nome, cpf, funcao, contato, data_contratacao,
             valor_diaria, observacao, id_contratante, id_despesas)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (nome, cpf, funcao, contato, data_contratacao,
              valor_diaria, observacao, id_contratante, id_despesas)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Membro de equipe cadastrado com sucesso!")