import mysql.connector
import sys
import os
# Sobe um nível (de Lista → Control)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector import conectar

def remove_patrocinadores(conexao):
    id = int(input('Digite o numero do cadastro que deseja remover: '))
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM patrocinadores WHERE id = %s', (id,))
    registro = cursor.fetchone()

    if not registro:
        print(f'Cadastro com ID {id} não encontrado.')
        return

    cursor.execute('DELETE FROM patrocinadores WHERE id = %s', (id,))
    conexao.commit()
    print(f'Registro {id} removido com sucesso.')