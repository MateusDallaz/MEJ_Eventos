import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_localRealizado(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM local_realizado WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome_local, capacidade_total, endereco FROM local_realizado')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    nome_local = input('Digite o novo nome do local: ')
    capacidade_total = int(input('Digite a nova capacidade total: '))
    endereco = input('Digite o novo endereço: ')

    cursor.execute(
        'UPDATE local_realizado SET nome_local = %s, capacidade_total = %s, endereco = %s WHERE id = %s',
        (nome_local, capacidade_total, endereco, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')