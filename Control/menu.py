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

from Delete.remove_contratante import remove_contratante
from Delete.remove_agenda import remove_agenda
from Delete.remove_marketing import remove_marketing
from Delete.remove_publico import remove_publico
from Delete.remove_patrocinadores import remove_patrocinadores
from Delete.remove_artista import remove_artista
from Delete.remove_despesas import remove_despesas
from Delete.remove_equipe import remove_equipe
from Delete.remove_financeiro import remove_financeiro
from Delete.remove_localRealizado import remove_localRealizado

from Join.join_contratante_marketing import join_contratante_marketing
from Join.join_contratante_equipe import join_contratante_equipe
from Join.join_agenda_artista import join_agendaArtista
from Join.join_agenda_local import join_agenda_local

from uptade.uptade_equipe import update_equipe
from uptade.uptade_agenda import update_agenda
from uptade.uptade_publico import update_publico
from uptade.uptade_financeiro import update_financeiro
from uptade.uptade_localrealizado import update_localRealizado
from uptade.uptade_marketing import update_marketing
from uptade.uptade_patrocinadores import update_patrocinadores
from uptade.uptade_contratante import update_contratante
from uptade.uptade_artista import update_artista
from uptade.uptade_despesas import update_despesas




from encerrar_conexao import fechar_conexao

def menu (conexao):
    while True :
        print("\n=== MENU PRINCIPAL ===")
        print('\n 1 - Cadastrar | 2 - Listar | 3 - Remover | 4 - Listagens Cruzadas | 5 - atualizar | 6 - Sair')
        opcao = input("Escolha a opção desejada: ")

        if opcao == '1':
            tabelas_cadastro = ["Contratante","Agenda","Artista","Despesas","Equipe","Financeiro","Local Realizado","Marketing","Patrocinadores","Público"]
            print("\n=== OPÇÕES DISPOSNIVEIS PARA CADASTROS ===\n")
            for i,tabelas_cadastro in enumerate (tabelas_cadastro, start=1):
                print(f'{i} - {tabelas_cadastro}')
            opcao_cadastro = input("Escolha uma tabela de cadastro (Digite 11 para sair): ")

            if opcao_cadastro == '1':
                print("\n=== CADASTRO DE CONTRATANTE ===")
                inserir_contratante(conexao)

            elif opcao_cadastro == '2':
                print("\n=== CADASTRO DE AGENDA ===")
                inserir_agenda(conexao)

            elif opcao_cadastro == '3':
                print("\n=== CADASTRO DE ARTISTA ===")
                inserir_artista(conexao)

            elif opcao_cadastro == '4':
                print("\n=== CADASTRO DE DESPESAS ===") 
                inserir_despesa(conexao)

            elif opcao_cadastro == '5':
                print("\n=== CADASTRO DE EQUIPE ===")
                inserir_equipe(conexao)

            elif opcao_cadastro == '6':
                print("\n=== CADASTRO DE FINANCEIRO ===")
                inserir_financeiro(conexao)

            elif opcao_cadastro == '7':
                print("\n=== CADASTRO DE LOCAL REALIZADO ===")
                inserir_local(conexao)

            elif opcao_cadastro == '8':
                print("\n=== CADASTRO DE MARKETING ===")
                inserir_marketing(conexao)

            elif opcao_cadastro == '9':
                print("\n=== CADASTRO DE PATROCINADORES ===")
                inserir_patrocinador(conexao)

            elif opcao_cadastro == '10':
                print("\n=== CADASTRO DE PÚBLICO ===")
                inserir_publico(conexao)
                
            elif opcao_cadastro == '11':
                print("\n=== Até logo! ===")
                break
                
            else:
                print('Digite uma opção valida')


        elif opcao == '2':
            tabelas_Lista = ["Contratante","Agenda","Artista","Despesas","Equipe","Financeiro","Local Realizado","Marketing","Patrocinadores","Público"]
            print ("\n=== TABELAS DISPONIVEIS PARA LISTAGEM ===\n")
            for i,tabela in enumerate(tabelas_Lista, start=1):
                print(f'{i} - {tabela}')
            opcao_listar = input("\nEscolha uma tabela para listar (Digite 11 para sair): ")

            if opcao_listar == '1':
                print("\n=== LISTAGEM DE CONTRATANTE ===")
                listagem_contratante(conexao)


            elif opcao_listar == '2':
                print("\n=== LISTAGEM DE AGENDA ===")
                listagem_agenda(conexao)

            elif opcao_listar == '3':
                print("\n=== LISTAGEM DE ARTISTA ===")
                listagem_artista(conexao)


            elif opcao_listar == '4':
                print("\n=== LISTAGEM DE DESPESAS ===")
                listagem_despesas(conexao)


            elif opcao_listar == '5':
                print("\n=== LISTAGEM DE EQUIPE ===")                  
                listagem_equipe(conexao)


            elif opcao_listar == '6':
                print("\n=== LISTAGEM DE FINANCEIRO ===")
                listagem_financeiro(conexao)


            elif opcao_listar == '7':
                print("\n=== LISTAGEM DE LOCAL REALIZADO ===")
                listagem_localRealizado(conexao)



            elif opcao_listar == '8':
                print("\n=== LISTAGEM DE MARKETING ===")
                listagem_marketing(conexao)


            elif opcao_listar == '9':
                print("\n=== LISTAGEM DE PATROCINADORES ===")
                listagem_patrocinadores(conexao)


            elif opcao_listar == '10':
                print("\n=== LISTAGEM DE PÚBLICO ===")
                listagem_publico(conexao)

            elif opcao_listar == '11':
                print("\n=== Até logo! ===")
                break;

            else:
                print ("Digite uma opção valida")

        elif opcao == '3':
            tabelas_Lista = ["Contratante","Agenda","Artista","Despesas","Equipe","Financeiro","Local Realizado","Marketing","Patrocinadores","Público"]
            print ("\n=== TABELAS DISPONIVEIS PARA REMOÇÃO ===\n")
            for i,tabela in enumerate(tabelas_Lista, start=1):
                print(f'{i} - {tabela}')
            opcao_remover = input("\nEscolha uma tabela para remover (Digite 11 para sair): ")

            if opcao_remover == '1':
                print('\n=== REMOÇÃO DE DADOS DE CONTRATANTE ===')
                listagem_contratante(conexao)
                remove_contratante(conexao)

            elif opcao_remover == '2':
                print('\n=== REMOÇÃO DE DADOS DE AGENDA ===')
                listagem_agenda(conexao)
                remove_agenda(conexao)

            elif opcao_remover == '3':
                print('\n=== REMOÇÃO DE DADOS DE ARTISTA ===')
                listagem_artista(conexao)
                remove_artista(conexao)
    
            elif opcao_remover == '4':
                print('\n=== REMOÇÃO DE DADOS DE DESPESAS ===')
                listagem_despesas(conexao)
                remove_despesas(conexao)

            elif opcao_remover == '5':
                print('\n=== REMOÇÃO DE DADOS DE EQUIPE ===')
                listagem_equipe(conexao)
                remove_equipe(conexao)

            elif opcao_remover == '6':
                print('\n=== REMOÇÃO DE DADOS DE FINANCEIRO ===')
                listagem_financeiro(conexao)
                remove_financeiro(conexao)

            elif opcao_remover == '7':
                print('\n=== REMOÇÃO DE DADOS DE LOCAL REALIZADO ===')
                listagem_localRealizado(conexao)
                remove_localRealizado(conexao)

            elif opcao_remover == '8':
                print('\n=== REMOÇÃO DE DADOS DE MARKETING ===')
                listagem_marketing(conexao)
                remove_marketing(conexao)

            elif opcao_remover == '9':
                print('\n=== REMOÇÃO DE DADOS DE PATROCINADORES ===')
                listagem_patrocinadores(conexao)
                remove_patrocinadores(conexao)

            elif opcao_remover == '10':
                print('\n=== REMOÇÃO DE DADOS DE PÚBLICO ===')
                listagem_publico(conexao)
                remove_publico(conexao)

            elif opcao_remover == '11':
                print("\n=== Até logo! ===")
                break;

            else:
                print ("Digite uma opção valida")


        elif opcao == '4':
            listagens_cruzadas = ["Contratante e Marketing","Contratante e Equipe", "Agenda e Artista", "Agenda e Local Realizado"]
            print ("\n=== LISTAGENS CRUZADAS DISPONIVEIS ===\n")
            for i,listagem in enumerate(listagens_cruzadas, start=1):
                print(f'{i} - {listagem}')
            opcao_listagem_cruzada = input("\nEscolha uma listagem cruzada para exibir (Digite 5 para sair): ")

            if opcao_listagem_cruzada == '1':
                print("\n=== LISTAGEM CRUZADA DE CONTRATANTE E MARKETING ===")
                join_contratante_marketing(conexao)

            elif opcao_listagem_cruzada == '2':
                print("\n=== LISTAGEM CRUZADA DE CONTRATANTE E EQUIPE ===")
                join_contratante_equipe(conexao)

            elif opcao_listagem_cruzada == '3':
                print("\n=== LISTAGEM CRUZADA DE AGENDA E ARTISTA ===")
                join_agendaArtista(conexao)

            elif opcao_listagem_cruzada == '4':
                print("\n=== LISTAGEM CRUZADA DE AGENDA E LOCAL REALIZADO ===")
                join_agenda_local(conexao)

            elif opcao_listagem_cruzada == '5':
                print("\n=== Até logo! ===")
                break;
            else:
                print ("Digite uma opção valida")

        elif opcao == '5':
            tabelas_Lista = ["Contratante","Agenda","Artista","Despesas","Equipe","Financeiro","Local Realizado","Marketing","Patrocinadores","Público"]
            print ("\n=== TABELAS DISPONIVEIS PARA ATUALIZAÇÃO ===\n")
            for i,tabela in enumerate(tabelas_Lista, start=1):
                print(f'{i} - {tabela}')
            opcao_atualizar = input("\nEscolha uma tabela para atualizar (Digite 11 para sair): ")

            if opcao_atualizar == '1':
                print('\n=== ATUALIZAÇÃO DE DADOS DE CONTRATANTE ===')
                listagem_contratante(conexao)
                update_contratante(conexao)

            elif opcao_atualizar == '2':
                print('\n=== ATUALIZAÇÃO DE DADOS DE AGENDA ===')
                listagem_agenda(conexao)
                update_agenda(conexao)

            elif opcao_atualizar == '3':
                print('\n=== ATUALIZAÇÃO DE DADOS DE ARTISTA ===')
                listagem_artista(conexao)
                update_artista(conexao)
    
            elif opcao_atualizar == '4':
                print('\n=== ATUALIZAÇÃO DE DADOS DE DESPESAS ===')
                listagem_despesas(conexao)
                update_despesas(conexao)

            elif opcao_atualizar == '5':
                print('\n=== ATUALIZAÇÃO DE DADOS DE EQUIPE ===')
                listagem_equipe(conexao)
                update_equipe(conexao)

            elif opcao_atualizar == '6':
                print('\n=== ATUALIZAÇÃO DE DADOS DE FINANCEIRO ===')
                listagem_financeiro(conexao)
                update_financeiro(conexao)

            elif opcao_atualizar == '7':
                print('\n=== ATUALIZAÇÃO DE DADOS DE LOCAL REALIZADO ===')
                listagem_localRealizado(conexao)
                update_localRealizado(conexao)

            elif opcao_atualizar == '8':
                print('\n=== ATUALIZAÇÃO DE DADOS DE MARKETING ===')
                listagem_marketing(conexao)
                update_marketing(conexao)

            elif opcao_atualizar == '9':
                print('\n=== ATUALIZAÇÃO DE DADOS DE PATROCINADORES ===')
                listagem_patrocinadores(conexao)
                update_patrocinadores(conexao)

            elif opcao_atualizar == '10':
                print('\n=== ATUALIZAÇÃO DE DADOS DE PÚBLICO ===')
                listagem_publico(conexao)
                update_publico(conexao)

            else:
                print ("Digite uma opção valida")
                return

        elif opcao == '6':
            fechar_conexao(conexao)
            break;
        else:
            print ("Opção inválida, tente novamente.")