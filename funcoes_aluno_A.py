import main
import funcoes_aluno_B

lista_eventos = []
lista_eventos_geral = []

def mostraEventoDetalhado (evento):
    print("Nome do evento:", evento["nome"])
    print("Data do evento:", evento["data"])
    print("Local do evento:", evento["local"])
    print("Categoria do evento:", evento["categoria"])
    print("\n")



def mostrar_eventos(lista_eventos):
    for evento in lista_eventos:
        print("Nome do Evento: ", evento["nome"])




# funcao de dar espaço entre resultados    
def espaco_vazio():
    print("")

def lerValoresEvento ():
    adicionar_evento_nome  = input("\ndigite o nome evento que voce deseja adicionar: ")
    adicionar_evento_data  = input("\ndigite a data de realização dele: ")
    adicionar_evento_local  = input("\ndigite o local onde acontecera o evento: ")
    adicionar_evento_genero  = input("\ndigite qual o tipo de evento: ")
    return adicionar_evento_nome, adicionar_evento_data, adicionar_evento_local, adicionar_evento_genero

# função para adicionar listas
def adicionarEvento(listaEventos, nome, data, local, categoria):            
    evento = {
        "nome": nome ,
        "data": data,
        "local": local,
        "categoria": categoria
    }
    listaEventos.append(evento)
        
        
#funcao de mostra a lista de eventos


def menu_adicionar_evento():
    while True:
        print("1. Mostrar os eventos atuais")
        print("2. Adicionar um evento a sua lista de eventos")
        print("3. sair\n")

        opcao =  input("digite a opção desejada: ")
        if opcao == '1':
            espaco_vazio()
            mostrar_eventos()
            espaco_vazio()
            main.enter_confirm()
            espaco_vazio()

        elif opcao == '2':
            adicionarEvento()

        elif opcao == '3':
            print("\ntchau :)\n")
            break
        
        else:
            espaco_vazio()
            print("voce nao digitou nenhum carctere disponivel, tente novamente")
            espaco_vazio()
    

