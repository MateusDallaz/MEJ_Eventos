import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_artista(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM artista WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, contatos, descricao FROM artista')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    print(f'Registro encontrado: {registro}')

    nome = input('Digite o novo nome do artista: ')
    contatos = input('Digite os novos contatos do artista: ')
    preferencias = input('Digite as novas preferências do artista: ')
    descricao = input('Digite a nova descrição do artista: ')

    cursor.execute(
        'UPDATE artista SET nome = %s, contatos = %s, preferencias = %s, descricao = %s WHERE id = %s',
        (nome, contatos, preferencias, descricao, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')