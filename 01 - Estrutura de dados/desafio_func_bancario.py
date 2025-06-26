def exibir_menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ======================================
    => """
    return input(menu).lower()

def depositar(saldo, extrato, /):
    """
    Realiza a operação de depósito.
    Recebe o saldo e o extrato e retorna os valores atualizados.
    """
    try:
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    except ValueError:
        print("\n@@@ Operação falhou! Por favor, insira um valor numérico. @@@")
    
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    Recebe os dados da conta como argumentos nomeados e retorna os valores atualizados.
    """
    try:
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print(f"\n@@@ Operação falhou! O valor do saque (R$ {valor:.2f}) excede o limite de R$ {limite:.2f}. @@@")
        elif excedeu_saques:
            print(f"\n@@@ Operação falhou! Número máximo de {limite_saques} saques excedido. @@@")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    except ValueError:
        print("\n@@@ Operação falhou! Por favor, insira um valor numérico. @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """Exibe o extrato da conta e o saldo final."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    """Função principal que executa o sistema bancário."""
    # Constantes
    LIMITE_SAQUES = 3
    
    # Variáveis de estado
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("\nSaindo do sistema... Obrigado por usar nosso banco!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()