import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_patrocinadores(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM patrocinadores WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome_empresa, descricao FROM patrocinadores')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    nome_empresa = input('Digite o novo nome da empresa: ')
    descricao = input('Digite a nova descrição: ')

    cursor.execute(
        'UPDATE patrocinadores SET nome_empresa = %s, descricao = %s WHERE id = %s',
        (nome_empresa, descricao, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')