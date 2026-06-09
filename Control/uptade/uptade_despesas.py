import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_despesas(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM despesas WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id,custo_contratacao, custo_local, custo_equipe, logistica, equipamento FROM despesas')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    custo_contratacao = float(input('Digite o novo custo de contratação: '))
    custo_local = float(input('Digite o novo custo do local: '))
    custo_equipe = float(input('Digite o novo custo da equipe: '))
    logistica = float(input('Digite o novo custo da logística: '))
    equipamento = float(input('Digite o novo custo do equipamento: '))

    cursor.execute(
        'UPDATE despesas SET custo_contratacao = %s, custo_local = %s, custo_equipe = %s, logistica = %s, equipamento = %s WHERE id = %s',
        (custo_contratacao, custo_local, custo_equipe, logistica, equipamento, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')