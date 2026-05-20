#Marketing

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar

def inserir_marketing(conexao):
    print("\n=== Cadastro de Marketing ===")
    meio_comunicacao = input("Meio de comunicação: ").strip()
    tipo_midia       = input("Tipo de mídia: ").strip()
    data_inicio      = input("Data início (AAAA-MM-DD): ").strip() or None
    data_fim         = input("Data fim (AAAA-MM-DD): ").strip() or None
    custo            = input("Custo: ").strip()
    alcance          = input("Alcance: ").strip()
    id_equipe        = pedir_fk(conexao, "equipe",      "Equipe",      ("id", "nome"))
    id_contratante   = pedir_fk(conexao, "contratante", "Contratante", ("id", "nome"))
 
    sql = """
        INSERT INTO marketing
            (meio_comunicacao, tipo_midia, data_inicio, data_fim,
             custo, alcance, id_equipe, id_contratante)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (meio_comunicacao, tipo_midia, data_inicio, data_fim,
              custo, alcance, id_equipe, id_contratante)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Ação de marketing cadastrada com sucesso!")