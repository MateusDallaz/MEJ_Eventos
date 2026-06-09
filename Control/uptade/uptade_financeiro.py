import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar


def update_financeiro(conexao):
    id = int(input('Digite o numero do cadastro que deseja atualizar: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT id, valor_evento, despesa_total, lucro_evento FROM financeiro')
    resultado = cursor.fetchall()
    for i in resultado:
        print(i)

    cursor.execute('SELECT * FROM financeiro WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        cursor.close()
        return

    print(f'Registro encontrado: {registro}')

    valor_evento = float(input('Digite o novo valor do evento: '))
    despesa_total = float(input('Digite a nova despesa total: '))
    lucro_evento = float(input('Digite o novo lucro do evento: '))

    cursor.execute(
        'UPDATE financeiro SET valor_evento = %s, despesa_total = %s, lucro_evento = %s WHERE id = %s',
        (valor_evento, despesa_total, lucro_evento, id)
    )
    conexao.commit()
    cursor.close()
    print(f'Registro {id} atualizado com sucesso.')