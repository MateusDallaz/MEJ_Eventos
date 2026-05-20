import mysql.connector

def pedir_fk(conexao, tabela, label, campos):
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
    id_artista= input("Código do Artista: ")
