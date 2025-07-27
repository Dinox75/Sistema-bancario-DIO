lista_compras = []

while True:
    print("==== Menu ====")
    print("\n1: Criar lista")
    print("2: Excluir lista")
    print("3: Ver listas")
    print("4: Editar lista")
    print("5: Sair")  
    print("\n==== Menu ====")

    opção = input("Escolha uma opção (de 1 a 5): ")
    
    if opção not in ['1', '2', '3', '4', '5']:
        print("Valor incorreto, insira um numero de 1 a 5")

    if opção == "1":
        nome_lista = input("Digite o nome da lista: ")
        nova_lista = {'nome': nome_lista, 'itens': []}
        lista_compras.append(nova_lista)
        print(f"Lista '{nome_lista}' criada com sucesso!")

    elif opção == "2":
        if len(lista_compras) == 0:
            print("Não há listas para excluir.")
        else:
            print("\nListas disponíveis:")
            for i, lista in enumerate(lista_compras):
                print(f"{i + 1}: {lista['nome']}")

            escolha = input("Digite o número da lista que deseja excluir: ")
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(lista_compras):
                    lista_compras.pop(indice)
                    print("Lista excluída com sucesso!")
                else:
                    print("Número inválido")
            except ValueError:
                print("Por favor, digite um número válido.")
                
    elif opção == '3':
        if len(lista_compras) == 0:
            print("Não há listas criadas")
        else:
            print("\nListas disponiveis:")
            for i, lista in enumerate(lista_compras):
                print(f"{i + 1}: {lista['nome']}")
                
    elif opção == '4':
        if len(lista_compras) == 0:
            print("Não há listas para editar.")
        else:
            print("\nListas disponiveis:")
            for i, lista in enumerate(lista_compras):
                print(f"{i + 1}: {lista['nome']}")
            
    else:
        print("Volte sempre!")
        break
