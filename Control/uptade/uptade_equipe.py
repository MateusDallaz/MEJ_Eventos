import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_equipe(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM equipe WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, nome, funcao, observacao FROM equipe')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    nome = input('Digite o novo nome do membro da equipe: ')
    funcao = input('Digite a nova função do membro da equipe: ')
    observacao = input('Digite a nova observação do membro da equipe: ')

    cursor.execute(
        'UPDATE equipe SET nome = %s, funcao = %s, observacao = %s WHERE id = %s',
        (nome, funcao, observacao, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')