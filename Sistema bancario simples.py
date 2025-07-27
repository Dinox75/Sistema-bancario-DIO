saldo = 0
limite = 724
extrato = ""
numero_saques = 0
limite_saques = 5

while True:
    print("Bem-vindo ao Banco Python!")
    print("Selecione uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        # Depositar
        valor = float(input("Digite o valor a ser depositado: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        # Sacar
        if numero_saques < limite_saques:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if 0 < valor <= saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para saque.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "3":
        # Extrato
        print("Extrato:")
        if extrato:
            print(extrato)
        else:
            print("Nenhuma transação realizada.")

    elif opcao == "4":
        print("Obrigado por usar o Banco Python!")
        break

    else:
        print("Opção inválida. Tente novamente.")