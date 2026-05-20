import mysql.connector

# Mapeamento padrão: tabela → coluna de exibição (quando não informada via parâmetro)
_COLUNA_LABEL = {
    "artista": "nome",
    "contratante": "nome",
    "equipe": "nome",
    "marketing": "nome",
    "patrocinadores": "nome_empresa",
    "local_realizado": "nome_local",
    "despesas": "custo_contratacao",
    "financeiro": "id",
    "publico": "id",
    "agenda": "nome_evento",
}


def pedir_fk(conexao, tabela, label, campos=None):
    # Define as colunas a consultar
    if campos is not None:
        col_id, col_label = campos
    else:
        col_id = "id"
        col_label = _COLUNA_LABEL.get(tabela.lower(), "id")

    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(f"SELECT `{col_id}`, `{col_label}` FROM `{tabela}`")
        registros = cursor.fetchall()
        cursor.close()
    except mysql.connector.Error as e:
        print(f"  [Aviso] Não foi possível consultar a tabela '{tabela}': {e}")
        valor = input(f"  Informe o ID do {label} manualmente (ou deixe vazio): ").strip()
        return int(valor) if valor.isdigit() else None

    # Tabela vazia
    if not registros:
        print(f"[Aviso] Nenhum registro encontrado em '{tabela}'.")
        valor = input(f"Informe o ID do {label} manualmente (ou deixe vazio): ").strip()
        return int(valor) if valor.isdigit() else None

    # Exibe os registros disponíveis
    print(f"\n--- {label}s disponíveis ---")
    for reg in registros:
        print(f"  {reg[col_id]:>4} | {reg[col_label]}")
    print()

    # Solicita a escolha
    while True:
        valor = input(f"ID do {label} (ou deixe vazio para nenhum): ").strip()

        if valor == "":
            return None

        if valor.isdigit():
            id_escolhido = int(valor)
            ids_validos = [reg[col_id] for reg in registros]
            if id_escolhido in ids_validos:
                return id_escolhido
            print(f"[Erro] ID {id_escolhido} não encontrado. Tente novamente.")
        else:
            print("[Erro] Digite apenas números ou deixe em branco.")