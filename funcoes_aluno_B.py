def displayMenu():
    print("\n=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")


def getEscolhaDoUsuario():
    try:
        return int(input("\nEscolha uma opção: "))
    except ValueError:
        return -1


def filtrarEventosPorCategoria(listaEventos, categoria):
    eventosFiltrados = []
    for evento in listaEventos:
        if evento["categoria"].strip().lower() == categoria.strip().lower():
            eventosFiltrados.append(evento)
    return eventosFiltrados


def marcarEventoAtendido(listaEventos, id_evento):
    indice = id_evento - 1
    if 0 <= indice < len(listaEventos):
        listaEventos[indice]["participado"] = True
        print(f"\n✅ Evento '{listaEventos[indice]['nome']}' marcado como participado!")
    else:
        print("\n❌ Evento não encontrado. Verifique o ID digitado.")


def gerarRelatorio(listaEventos):
    totalEventos = len(listaEventos)

    if totalEventos == 0:
        print("\n--- RELATÓRIO DE EVENTOS ---")
        print("Nenhum evento cadastrado para exibir no relatório.")
        return

    contagemCategorias = {}
    totalParticipados = 0

    for evento in listaEventos:
        cat = evento["categoria"]
        contagemCategorias[cat] = contagemCategorias.get(cat, 0) + 1
        if evento.get("participado", False):
            totalParticipados += 1

    percentualParticipados = (totalParticipados / totalEventos) * 100

    print("\n--- RELATÓRIO DE EVENTOS ---")
    print(f"Total de Eventos: {totalEventos}")
    print(f"Por Categoria: {contagemCategorias}")
    print(
        f"Participados: {percentualParticipados:.0f}% ({totalParticipados}/{totalEventos})"
    )