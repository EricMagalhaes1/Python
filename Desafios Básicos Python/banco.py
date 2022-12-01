menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = (float(input("Insira o valor que deseja depositar: ")))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R${valor:.2f} \n"
        else:
            print("Operação falhou, valor invalido.")

    elif opcao == "s":
        valor = (float(input("Insira o Valor que deseja sacar: ")))
        excedeu_saldo = valor > saldo      
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Você não possui limite suficiente.")
        
        elif excedeu_saque:
            print("Operação falhou! Limite de saques atingido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Operação falhou! Valor Invalido")
    
    elif opcao == "e":
       print("\n==================================== EXTRATO ====================================")
       print("Não foram realizadas transações " if not extrato else extrato)
       print(f"\n Saldo: R$ {saldo:.2f}")
       print("=================================================================================")
    
    elif opcao =="q":
        break