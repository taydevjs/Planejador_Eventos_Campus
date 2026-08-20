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
    categoria_busca = categoria.strip().lower()
    return [
        evento for evento in listaEventos 
        if evento.get("categoria", "").strip().lower() == categoria_busca
    ]


def marcarEventoAtendido(listaEventos, id_evento):
    for evento in listaEventos:
        if evento.get("id") == id_evento or listaEventos.index(evento) == id_evento - 1:
            evento["participado"] = True
            print(f"\n✅ Evento '{evento.get('nome')}' marcado como participado!")
            return
            
    print("\n❌ Evento não encontrado. Verifique o ID digitado.")


def gerarRelatorio(listaEventos):
    totalEventos = len(listaEventos)

    if not totalEventos:
        print("\n--- RELATÓRIO DE EVENTOS ---")
        print("Nenhum evento cadastrado para exibir no relatório.")
        return

    contagemCategorias = {}
    totalParticipados = 0

    for evento in listaEventos:
        cat = evento.get("categoria", "Sem Categoria")
        contagemCategorias[cat] = contagemCategorias.get(cat, 0) + 1
        totalParticipados += 1 if evento.get("participado") else 0

    percentualParticipados = (totalParticipados / totalEventos) * 100

    print("\n--- RELATÓRIO DE EVENTOS ---")
    print(f"Total de Eventos: {totalEventos}")
    print("Por Categoria:")
    for cat, qtd in contagemCategorias.items():
        print(f"  - {cat}: {qtd}")
    print(
        f"Participados: {percentualParticipados:.0f}% ({totalParticipados}/{totalEventos})"
    )