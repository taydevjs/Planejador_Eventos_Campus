def displayMenu():
    print("=== Planejador de Eventos do Campus ===")
    print("1. Adicionar Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Sair")

def getEscolhaDoUsuario():
    try:
        escolha = int(input("\nEscolha uma opção: "))
        return escolha
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
        return -1

def filtrarEventosPorCategoria(listaEventos, categoria):
    encontrados = [e for e in listaEventos if e.get("categoria", "").strip().lower() == categoria.strip().lower()]
    
    if not encontrados:
        print(f"\nNenhum evento encontrado para a categoria '{categoria}'.")
        return
    
    print(f"\n--- EVENTOS DA CATEGORIA: {categoria.capitalize()} ---")
    for e in encontrados:
        status = "Participado" if e.get("participado", False) else "Pendente"
        print(f"ID: {e.get('id')} | Nome: {e.get('nome')} | Data: {e.get('data')} | Local: {e.get('local')} | Status: {status}")

def marcarEventoAtendido(listaEventos, id_evento):
    for e in listaEventos:
        if e.get("id") == id_evento:
            e["participado"] = True
            print(f"\nEvento '{e.get('nome')}' marcado como participado com sucesso!")
            return
    print(f"\nEvento com ID {id_evento} não foi encontrado.")
    
   


