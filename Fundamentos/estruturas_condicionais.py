Maior_Idade = 18
Idade_Especial = 17

idade = int(input("Informe sua idade: "))

if idade >= Maior_Idade:
    print("Maior de idade, pode tirar a CNH.")

if idade< Maior_Idade:
    print("Ainda não pode tirar a CNH.")


if idade >= Maior_Idade:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.") 

if idade >= Maior_Idade:
    print("Maior de idade, pode tirar a CNH.")
elif idade == Idade_Especial:
    print("Pode fazer as provas teoricas, mas não as praticas")
else:
    print("Ainda não pode tirar a CNH.  ") 
