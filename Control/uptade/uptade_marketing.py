import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_marketing(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM marketing WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, meio_comunicacao, tipo_midia, alcance FROM marketing')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    meio_comunicacao = input('Digite o novo meio de comunicação: ')
    tipo_midia = input('Digite o novo tipo de mídia: ')
    alcance = int(input('Digite o novo alcance: '))

    cursor.execute(
        'UPDATE marketing SET meio_comunicacao = %s, tipo_midia = %s, alcance = %s WHERE id = %s',
        (meio_comunicacao, tipo_midia, alcance, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')