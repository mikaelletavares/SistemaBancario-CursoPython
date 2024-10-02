saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    valor = float(input("\nInforme o valor que deseja depositar: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito: R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")

def sacar():
    global saldo, extrato, numero_saques
    valor = float(input("\nInforme o valor que deseja sacar: "))

    if valor > saldo:
        print("Erro... Você não tem saldo suficiente!")
    elif valor > limite:
        print("Erro... O valor do saque é maior que o limite!")
    elif numero_saques >= LIMITE_SAQUES:
        print("Erro... Número de saques excedido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"dSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("O valor informado é inválido.")

def ver_extrato():
    global saldo, extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    menu = '''
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    '''

    while True:
        opcao = input(menu)
        if opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            ver_extrato()
        elif opcao == "q":
            print("Até a próxima! :D")
            break
        else:
            print("Operação inválida!")

if __name__ == "__main__":
    main()
