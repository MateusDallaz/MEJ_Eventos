import mysql.connector
from connector import conectar

from Cadastro.cadastro_contratante import inserir_contratante
from Cadastro.cadastro_despesas import inserir_despesa
from Cadastro.cadastro_equipe import inserir_equipe
from Cadastro.cadastro_artista import inserir_artista
from Cadastro.cadastro_financeiro import inserir_financeiro
from Cadastro.cadastro_local_realizado import inserir_local
from Cadastro.cadastro_agenda import inserir_agenda
from Cadastro.cadastro_marketing import inserir_marketing
from Cadastro.cadastro_patrocinadores import inserir_patrocinador
from Cadastro.cadastro_publico import inserir_publico


from Lista.list_agenda import listagem_agenda
from Lista.list_artista import listagem_artista
from Lista.list_contratante import listagem_contratante
from Lista.list_despesas import listagem_despesas
from Lista.list_equipe import listagem_equipe
from Lista.list_financeiro import listagem_financeiro
from Lista.list_localRealizado import listagem_localRealizado
from Lista.list_marketing import listagem_marketing
from Lista.list_patrocinadores import listagem_patrocinadores
from Lista.list_publico import listagem_publico

def menu (conexao):
    while True :
        print ('\ n1 - cadastrar | 2 - listar | 3 - finalizar')
        opcao = input ("  escolha uma opção  ")

        if opcao == '1':
            tabelas_cadastro = ["contratante","agenda","artista","despesas","equipe","financeiro","local_realizado","marketing","patrocinadores","publico"]
            print("\n=== OPÇÕES DISPOSNIVEIS PARA CADASTROS ===")
            for i,tabelas_cadastro in enumerate (tabelas_cadastro = 1):
                print(f'{i}.{tabelas_cadastro}')
                opcao_cadastro = input("Escolha uma tabela de cadastro (Digite 11 para sair): ")

            if opcao_cadastro == 1:
                inserir_contratante(conexao);


            elif opcao_cadastro == '2':
                 inserir_agenda(conexao);


            elif opcao_cadastro == '3':
                 inserir_artista(conexao);


            elif opcao_cadastro == '4':
                inserir_despesa(conexao);


            elif opcao_cadastro == '5':
                inserir_equipe(conexao);


            elif opcao_cadastro == '6':
               inserir_financeiro(conexao);



            elif opcao_cadastro == '7':
               inserir_local(conexao);



            elif opcao_cadastro == '8':
                inserir_marketing(conexao);


            elif opcao_cadastro == '9':
                inserir_patrocinador(conexao);


            elif opcao_cadastro == '10':
                inserir_publico(conexao);
            
            elif opcao_cadastro == '11':
                break
            
            else:
                print('Digite uma opçao valida')


        elif opcao == '2':
            tabelas = ["contratante","agenda","artista","despesas","equipe","financeiro","local_realizado","marketing","patrocinadores","publico"]
            print ("\n=== TABELAS DISPONIVEIS PARA LISTAGEM ===")
            for i,tabela in enumerate (tabelas = 1):
             print(f'{i}.{tabela}')
             opcao_listar = input("escolha uma tabela para listar (Digite 11 para sair): ")

            if opcao_listar == 1:
                listagem_contratante(conexao);


            elif opcao_listar == '2':
                listagem_agenda(conexao);


            elif opcao_listar == '3':
                listagem_artista(conexao);


            elif opcao_listar == '4':
                listagem_despesas(conexao);


            elif opcao_listar == '5':
                listagem_equipe(conexao);


            elif opcao_listar == '6':
               listagem_financeiro(conexao);


            elif opcao_listar == '7':
               listagem_localRealizado(conexao);



            elif opcao_listar == '8':
                listagem_marketing(conexao);


            elif opcao_listar == '9':
                listagem_patrocinadores(conexao);


            elif opcao_listar == '10':
                listagem_publico(conexao);

            elif opcao_listar == '11':
                break;

            else:
                print ("Digite uma opção valida")

        elif opcao == '3':
            break;
        else:
            print ("opcao invalidade");


