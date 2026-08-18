lista_eventos = []

#função de mostra a lista de eventos
def mostrar_eventos():
    print(lista_eventos)

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
        espaco_vazio()
        adicionar_evento  = input("\ndigite o evento que voce deseja adicionar: ")
        lista_eventos.append(adicionar_evento)
        espaco_vazio()
        mostrar_eventos()
        espaco_vazio()
        enter_confirm()
        espaco_vazio()

    elif opcao == '3':
        print("\ntchau :)\n")
        break
    
    else:
        print("voce nao digitou nenhum carctere disponivel")
        break
    

