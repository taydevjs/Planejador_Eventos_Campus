import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principla():
    while True:
        print("""
        === Planejador de Eventos do Campus ===
        1. Adicionar Evento
        2. Ver Todos os Eventos
        3. Filtrar por Categoria
        4. Marcar Evento como Participado
        5. Gerar Relatório
        6. Sair 
        """)

        opcoes = input("Digite o numero da opção que deseja: ")

        if opcoes == "1":
            limpar_tela()
            
        elif opcoes == "2":
            limpar_tela()

        elif opcoes == "3":
            limpar_tela()

        elif opcoes == "4":
            limpar_tela()

        elif opcoes == "5":
            limpar_tela()

        elif opcoes == "6":
            limpar_tela()
