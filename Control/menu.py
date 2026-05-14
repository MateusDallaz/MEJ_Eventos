import _mysql_connector
from connector import conectar

def menu (conexao):
    while True :
        print ('\ n1 - cadastrar | 2 - listar | 3 - finalizar')
        opcao = input ("  escolha uma opção  ")

        if opcao == '1':
           inserir_cadastro()

        elif opcao == '2':
            tabelas = ["contratante","agenda","artista","despesas","equipe","financeiro","local_realizado","marketing","patrocinadores","publico"]
            print ("\n=== TABELAS DIPOSNIVEIS ===")
            for i,tabela in enumerate (tabelas = 1):
             print(f'{i}.{tabela}')
             opcao_listar = input("escolha uma tabela")

            if opcao_listar == 1:


            elif opcao_listar == '2':


            elif opcao_listar == '3':


            elif opcao_listar == '4':


            elif opcao_listar == '5':


            elif opcao_listar == '6':


            elif opcao_listar == '7':


            elif opcao_listar == '8':


            elif opcao_listar == '9':


            elif opcao_listar == '10':

            else:
                break;

        elif opcao == '3':
            break;
        else:
            print ("opcao invalidade");


