#Publico
import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from connector import conectar
from listagem_fk import pedir_fk

def inserir_publico(conexao):
    cabecalho("CADASTRO DE PÚBLICO ALVO")
 
    publico_alvo     = input("  Público alvo (ex: jovens, família, corporativo): ").strip() or None
    ingresso_vendido = input("  Ingressos vendidos: ").strip() or None
    observacao       = input("  Observação: ").strip() or None
    faixa_etaria     = input("  Faixa etária (ex: 18+, livre, 12-17): ").strip() or None
    tipo_ingresso    = input("  Tipo de ingresso (ex: pista, vip, camarote): ").strip() or None
    id_contratante   = pedir_fk(conexao, "contratante", "Contratante")
    id_artista       = pedir_fk(conexao, "artista",     "Artista")
 
    sql = """
        INSERT INTO publico
            (publico_alvo, ingresso_vendido, observascao,
             faixa_etaria, tipo_ingresso, id_contratante, id_artista)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    executar_insert(conexao, sql,
        (publico_alvo, ingresso_vendido, observacao,
         faixa_etaria, tipo_ingresso, id_contratante, id_artista))