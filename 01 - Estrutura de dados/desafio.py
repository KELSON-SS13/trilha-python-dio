
saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

menu = """
================ MENU ================
[d]\tDepositar
[s]\tSacar
[e]\tExtrato
[q]\tSair
=> """

while True:
    opcao = input(menu).lower() 

    if opcao == "d":
        print("--- Depósito ---")
        try:
            valor_deposito = float(input("Informe o valor do depósito: R$ "))

            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
                print("\nDepósito realizado com sucesso!")
            else:
                print("\nOperação falhou! O valor informado é inválido.")

        except ValueError:
            print("\nOperação falhou! Por favor, insira um número válido.")

    elif opcao == "s":
        print("--- Saque ---")
        try:
            valor_saque = float(input("Informe o valor do saque: R$ "))

            excedeu_saldo = valor_saque > saldo
            excedeu_limite_valor = valor_saque > limite_por_saque
            excedeu_limite_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

            if excedeu_saldo:
                print(f"\nOperação falhou! Saldo insuficiente. (Saldo atual: R$ {saldo:.2f})")

            elif excedeu_limite_valor:
                print(f"\nOperação falhou! O valor do saque excede o limite de R$ {limite_por_saque:.2f} por operação.")

            elif excedeu_limite_saques:
                print(f"\nOperação falhou! Número máximo de {LIMITE_SAQUES_DIARIOS} saques diários foi excedido.")

            elif valor_saque <= 0:
                print("\nOperação falhou! O valor informado é inválido.")

            else:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
                print("\nSaque realizado com sucesso!")

        except ValueError:
            print("\nOperação falhou! Por favor, insira um número válido.")


    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual:\tR$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Obrigado por usar nosso sistema. Até logo!")
        break

    else:
        print("Operação inválida! Por favor, selecione uma das opções do menu.")
