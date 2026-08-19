import os
from funcoes_aluno_B import (
    displayMenu,
    getEscolhaDoUsuario,
    filtrarEventosPorCategoria,
    marcarEventoAtendido,
    gerarRelatorio,
)


try:
    from funcoes_aluno_A import adicionar_evento
except ImportError:
    # Caso a função do Estudante A tenha outro nome ou ainda não esteja implementada:
    def adicionar_evento(listaEventos):
        nome = input("Nome do evento: ")
        data = input("Data (AAAA-MM-DD): ")
        local = input("Local: ")
        categoria = input("Categoria: ")

        novo_evento = {
            "nome": nome,
            "data": data,
            "local": local,
            "categoria": categoria,
            "participado": False,
        }
        listaEventos.append(novo_evento)
        print("\nEvento adicionado com sucesso!")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    listaEventos = []

    while True:
        displayMenu()
        opcao = getEscolhaDoUsuario()

        if opcao == 1:
            adicionar_evento(listaEventos)

        elif opcao == 2:
            print("\n--- TODOS OS EVENTOS ---")
            if not listaEventos:
                print("Nenhum evento cadastrado.")
            else:
                for index, evento in enumerate(listaEventos, start=1):
                    status = "[X]" if evento.get("participado", False) else "[ ]"
                    print(
                        f"{index}. {status} {evento['nome']} - {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']}"
                    )

        elif opcao == 3:
            categoriaBusca = input("Digite a categoria para filtrar: ")
            filtrados = filtrarEventosPorCategoria(listaEventos, categoriaBusca)

            print(f"\n--- EVENTOS DA CATEGORIA '{categoriaBusca}' ---")
            if not filtrados:
                print("Nenhum evento encontrado nesta categoria.")
            else:
                for evento in filtrados:
                    status = "[X]" if evento.get("participado", False) else "[ ]"
                    print(
                        f"- {status} {evento['nome']} ({evento['data']}) em {evento['local']}"
                    )

        elif opcao == 4:
            if not listaEventos:
                print("\nNenhum evento cadastrado para marcar.")
            else:
                try:
                    id_evento = int(
                        input("Digite o número (ID) do evento que participou: ")
                    )
                    marcarEventoAtendido(listaEventos, id_evento)
                except ValueError:
                    print("\n❌ Por favor, informe um número válido.")

        elif opcao == 5:
            gerarRelatorio(listaEventos)

        elif opcao == 6:
            print("\nSaindo do Planejador de Eventos. Até logo!")
            break

        else:
            print("\n❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()