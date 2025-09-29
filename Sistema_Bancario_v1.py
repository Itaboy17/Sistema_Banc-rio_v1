#Sistema bancário versão 1
#Variáveis
saldo = 10000.00
saque = -1
deposito = 0.00
qntd_saques = 0
qntd_depositos = 0
LIM_SAQUE_DIARIO = 3
LIM_VALOR_SAQUE = 500
extrato = ""
menu = '''
=======================
    Bamko Manikômico

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=======================
'''
mensagem = "\nEH U MANIKAS HEHE"

#Estrutura principal
while True:
    print(menu)
    option = input("Selecione a opção desejada: ")
    saque = -1

    if option == "d": #deposito
        print(f"\nSaldo Atual: R${saldo:.2f}\n")
        deposito = float(input("Valor que desejas depositar: R$ "))

        if deposito >= 0:
            saldo += deposito
            qntd_depositos += 1
            extrato += f"Depósito {qntd_depositos}: R${deposito:.2f}\n"
            print(f"Depósito de R${deposito:.2f} realizado com sucesso seu saldo agora é de: R${saldo:.2f}")
            print(mensagem)

        else:
            print("Insira um valor válido para depósito!")

    elif option == "s": #saque
        while saque < 0:
            print("\nInsira um valor válido para saque!")
            saque = float(input("Valor: R$"))

        if saque <= saldo:
            if qntd_saques < LIM_SAQUE_DIARIO:
                
                if saque >= 0 and saque <= LIM_VALOR_SAQUE:
                    saldo -= saque 
                    qntd_saques += 1
                    extrato += f"Saque diário {qntd_saques}: R${saque:.2f}"
                    print(f"\nSaque de R${saque:.2f} realizado com sucesso seu saldo agora é R${saldo:.2f}")
                    print(f"Você realizou {qntd_saques} hoje, lhe restam {LIM_SAQUE_DIARIO - qntd_saques}")
                    print(mensagem)

            else:
                print("Você não pode mais sacar hoje. Espere até que seus saques sejam liberados novamente.")
                print(mensagem)

        else:
            print(f"\nSeu saldo atual é de R${saldo:.2f}")
            print("Você não tem esse saldo para sacar")

    elif option == "e":
        print("\n=========== EXTRATO ===========")

        if qntd_depositos == 0 and qntd_saques == 0:
            print(f"Saldo: R${saldo:.2f}")
            print("Não foram realizadas movimentações")
        
        else:
            print(f"Saldo: R$ {saldo:.2f}\n")
            print(extrato)
            print("===============================")
            print(mensagem)

    elif option == "q":
        print(mensagem)
        break

    else:
        print("Operação inválida. Insira uma opção válida para que possas ser atendido!")