menu = """

[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opçao = (input(menu))

    if opçao == "1":
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
    
        else:
            print('Operação falhou! O valor informado é inválido.')


    elif opçao == "2":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Você não possui saldo suficiente.')


        elif excedeu_limite: 
            print('Operação falhou! O valor de saque excede o limite.')


        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        else:
            print("Opção falhou! O valor informado é inválido.")

    elif opçao == "3":
        print('\n***************EXTRATO********************')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('********************************************')

    elif opçao == "0":
        break

    else:
        print("Operação inválida! Por favor, selecione novamente a opção desejada.")
    


