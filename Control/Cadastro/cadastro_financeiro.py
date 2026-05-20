#Financeiro

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar
from listagem_fk import pedir_fk

def inserir_financeiro(conexao):
    print("\n=== Cadastro Financeiro ===")
    id_despesas       = pedir_fk(conexao, "despesas", "Despesa", ("id", "custo_contratacao"))
    valor_evento      = input("Valor do evento: ").strip()
    metodo_pagamento  = input("Método de pagamento: ").strip()
    despesa_total     = input("Despesa total: ").strip()
    lucro_evento      = input("Lucro do evento: ").strip()
 
    sql = """
        INSERT INTO financeiro
            (id_despesas, valor_evento, metodo_pagamento,
             despesa_total, lucro_evento)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (id_despesas, valor_evento, metodo_pagamento,
              despesa_total, lucro_evento)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Registro financeiro inserido com sucesso!")