#AGENDA

import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar
from listagem_fk import pedir_fk

def inserir_agenda(conexao):
    print("\n=== Cadastro de Agenda ===")
    data_evento       = input("Data do evento (AAAA-MM-DD): ").strip() or None
    data_agendamento  = input("Data do agendamento (AAAA-MM-DD): ").strip() or None
    nome_evento       = input("Nome do evento: ").strip()
    descricao         = input("Descrição: ").strip()
    id_contratante    = pedir_fk(conexao, "contratante", "Contratante")
    id_artista        = pedir_fk(conexao, "artista",     "Artista")
    id_local          = pedir_fk(conexao, "localrealizado", "Local", ("id", "nome_local"))
 
    sql = """
        INSERT INTO agenda
            (data_evento, data_agendamento, nome_evento, descricao,
             id_contratante, id_artista, id_local)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (data_evento, data_agendamento, nome_evento, descricao,
              id_contratante, id_artista, id_local)
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("✔  Agenda registrada com sucesso!")
 