import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_contratante(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM contratante WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, endereco, data_evento, contatos FROM contratante')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    nome = input('Digite o novo nome do contratante: ')
    endereco = input('Digite o novo endereço do contratante: ')
    data_evento = input('Digite a nova data do evento: ')
    contatos = input('Digite os novos contatos do contratante: ')

    cursor.execute(
        'UPDATE contratante SET nome = %s, endereco = %s, data_evento = %s, contatos = %s WHERE id = %s',
        (nome, endereco, data_evento, contatos, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')