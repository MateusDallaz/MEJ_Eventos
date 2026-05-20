import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar
from listagem_fk import pedir_fk


def inserir_despesa(conexao):
    custo_contratacao = input("Custo de contratação: ")
    custo_local = input("Custo do local: ")
    custo_equipe = input("Custo da equipe: ")
    logistica = input("Logística: ")
    equipamento = input("Equipamento: ")

    # 4. (Opcional) Artista – se a tabela existir
    resp = input("Associar a um artista? (s/N): ").lower()
    if resp == 's':
        cursor.execute("SELECT id, nome FROM artista")  # ajuste se não existir
        artistas = cursor.fetchall()
        if artistas:
            print("\n--- Artistas ---")
            for a in artistas:
                print(f"ID: {a['id']} - {a['nome']}")
            try:
                id_artista = int(input("ID do artista: "))
            except:
                pass
        else:
            print("Tabela artista vazia ou inexistente.")
    id_artista= input("Código do Artista: ")

    # 5. (Opcional) Contratante – se a tabela existir

    
    resp = input("Associar a um Contratante? (s/N): ").lower()
    if resp == 's':
        cursor.execute("SELECT id, nome FROM contratante")  # ajuste se não existir
        artistas = cursor.fetchall()
        if artistas:
            print("\n--- Contratante ---")
            for a in artistas:
                print(f"ID: {a['id']} - {a['nome']}")
            try:
                id_contratante = int(input("ID do contratante: "))
            except:
                pass
        else:
            print("Tabela contratante vazia ou inexistente.")
    id_contratante = input("Código do Contratante: ")
    
    sql = """INSERT INTO despesas 
             (custo_contratacao, custo_local, custo_equipe, logistica, equipamento, id_contratante, id_artista)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (custo_contratacao, custo_local, custo_equipe, logistica, equipamento, id_contratante, id_artista)
   
    cursor = conexao.cursor()
    cursor.execute(sql, values)
    conexao.commit()
    print("Registro inserido com sucesso!")