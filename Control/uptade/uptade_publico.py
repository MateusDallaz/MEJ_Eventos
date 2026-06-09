import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def update_publico(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM publico WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return
    cursor = conexao.cursor()
    cursor.execute('SELECT id, publico_alvo, ingresso_vendido, observacao, faixa_etaria FROM publico')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    publico_alvo = input('Digite o novo público-alvo: ')
    ingresso_vendido = int(input('Digite o novo número de ingressos vendidos: '))
    observacao = input('Digite a nova observação: ')
    faixa_etaria = input('Digite a nova faixa etária: ')

    cursor.execute(
        'UPDATE publico SET publico_alvo = %s, ingresso_vendido = %s, observacao = %s, faixa_etaria = %s WHERE id = %s',
        (publico_alvo, ingresso_vendido, observacao, faixa_etaria, id)
    )
    conexao.commit()
    print(f'Registro {id} atualizado com sucesso.')