

N = int(input("Digite o numero N: "))

while N > 0:
    A = input("Digite o numero A: ")
    B = input("Digite o numero B: ")
    A_Tamanho = len(A)
    B_Tamanho = len(B)
    if A[A_Tamanho - B_Tamanho:A_Tamanho] == B:
        print("encaixa")
    else:
        print("nao encaixa")
    N -= 1