
lista_eventos = []
lista_eventos_geral = []

#função de mostra a lista de eventos
def mostrar_eventos():
    print(lista_eventos_geral)

# função para confirmar no enter
def enter_confirm():
    verificar_enter = input("digite ENTER para continuar...")
    if verificar_enter == ' ':
        return 0
    else:
        print("Voce nao apertou enter")

# função de dar espaço entre resultados    
def espaco_vazio():
    print("")

# função para adicionar listas
def adicionar_evento():
        adicionar = list()
        adicionar_evento_nome  = input("\ndigite o nome evento que voce deseja adicionar: ")
        adicionar_evento_data  = input("\ndigite a data de realização dele: ")
        adicionar_evento_local  = input("\ndigite o local onde acontecera o evento: ")
        adicionar_evento_genero  = input("\ndigite qual o tipo de evento: ")
        adicionar.append(adicionar_evento_nome)
        adicionar.append(adicionar_evento_data)
        adicionar.append(adicionar_evento_local)
        adicionar.append(adicionar_evento_genero)
        lista_eventos_geral.append(adicionar)
        espaco_vazio()
        mostrar_eventos()
        espaco_vazio()
        enter_confirm()
        espaco_vazio()

while True:
    print("1. Mostrar os eventos atuais")
    print("2. Adicionar um evento a sua lista de eventos")
    print("3. sair\n")

    opcao =  input("digite a opção desejada: ")
    if opcao == '1':
        espaco_vazio()
        mostrar_eventos()
        espaco_vazio()
        enter_confirm()
        espaco_vazio()

    elif opcao == '2':
        adicionar_evento()

    elif opcao == '3':
        print("\ntchau :)\n")
        break
    
    else:
        espaco_vazio()
        print("voce nao digitou nenhum carctere disponivel, tente novamente")
        espaco_vazio()
    

