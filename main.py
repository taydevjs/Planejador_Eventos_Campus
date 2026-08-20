import os
import funcoes_aluno_A

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def displayMenu():
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair ")

def menu_principal():

    while True:
        
        displayMenu()   

        opcoes = input("Digite o numero da opção que deseja: ")

        if opcoes == '1':
            limpar_tela()
            nome , data, local , genero = funcoes_aluno_A.lerValoresEvento()
            funcoes_aluno_A.adicionar_evento(funcoes_aluno_A.lista_eventos, nome, data , local , genero)
            print("teste01")
            
        elif opcoes == '2':
            limpar_tela()
            print("teste02")
        elif opcoes == '2':
            limpar_tela()
            print("teste03")
        elif opcoes == '4':
            limpar_tela()
            print("teste04")

        elif opcoes == '5':
            limpar_tela()
            print("teste05")

        elif opcoes == '6':
            limpar_tela()
            print("teste06")
        
        else:
            limpar_tela()
            print("opcao digitada nao é valida")

if __name__ == "__main__":
    menu_principal()