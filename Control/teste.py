lista = ['agenda', 'artista', 'contratante', 'despesas', 'equipe', 'financeiro', 'local_realizado', 'marketing', 'patrocinadores', 'publico']

for i, tabelas in enumerate(lista, 1):
    print(f'{i}. {tabelas}')

tabela = input('Qual tabela deseja listar: ')

print (tabela)