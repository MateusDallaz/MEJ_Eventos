import mysql.connector
from mysql.connector import Error


def inserir_despesas(conexao):
    cursor = conexao.cursor(dictionary=True)
    
    # 1. Listar contratantes disponíveis
    cursor.execute("SELECT id, nome FROM contratante")
    contratantes = cursor.fetchall()
    if not contratantes:
        print("Nenhum contratante cadastrado. Cadastre um primeiro.")
        cursor.close()
        return
    
    print("\n--- Contratantes disponíveis ---")
    for c in contratantes:
        print(f"ID: {c['id']} - {c['nome']}")
    
    # 2. Escolher o contratante
    while True:
        try:
            id_contratante = int(input("ID do contratante: "))
            cursor.execute("SELECT id FROM contratante WHERE id = %s", (id_contratante,))
            if cursor.fetchone():
                break
            print("ID inválido.")
        except ValueError:
            print("Digite um número.")
    
    # 3. Coletar os custos
    print("\n--- Custos da despesa ---")
    custo_contratacao = float(input("Custo de contratação: ") or 0)
    custo_local      = float(input("Custo do local: ") or 0)
    custo_equipe     = float(input("Custo da equipe: ") or 0)
    logistica        = float(input("Logística: ") or 0)
    equipamento      = float(input("Equipamento: ") or 0)
    
    # 4. (Opcional) Artista – se a tabela existir
    id_artista = None
    resp = input("Associar a um artista? (s/N): ").lower()
    if resp == 's':
        cursor.execute("SELECT id, nome FROM artista")  # ajuste se não existir
        artistas = cursor.fetchall()
        if artistas:
            print("\n--- Artistas ---")
            for a in artistas:
                print(f"ID: {a['id']} - {a['nome']}")
            try:
                id_artista = int(input("ID do artista: "))
            except:
                pass
        else:
            print("Tabela artista vazia ou inexistente.")
    
    # 5. Inserir na tabela despesas
    sql = """INSERT INTO despesas 
             (custo_contratacao, custo_local, custo_equipe, logistica, equipamento, id_contratante, id_artista)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    valores = (custo_contratacao, custo_local, custo_equipe, logistica, equipamento, id_contratante, id_artista)
    
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        print("Despesa inserida com sucesso!")
    except Error as e:
        print(f"Erro ao inserir: {e}")
    finally:
        cursor.close()

# Uso
if _name_ == "_main_":
    conn = conectar()
    if conn:
        inserir_despesas(conn)
        conn.close()