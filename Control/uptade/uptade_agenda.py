import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_agenda(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM agenda WHERE id = %s', (id,))
    registro = cursor.fetchone()

    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome_evento, data_evento, descricao FROM agenda')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)
    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    print(f'Registro encontrado: {registro}')

    nome_evento = input('Digite o novo nome do evento: ')
    data_evento = input('Digite a nova data do evento: ')
    descricao = input('Digite a nova descrição do evento: ')

    cursor.execute(
        'UPDATE agenda SET nome_evento = %s, data_evento = %s, descricao = %s WHERE id = %s',
        (nome_evento, data_evento, descricao, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')