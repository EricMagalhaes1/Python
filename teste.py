N = input("Insira um numero: ")

while(N > 0):
    N = str(N)
    P = N.split(" ")
    A = P[0]
    B = P[1]
    C = len(B)
    if A[-C] == B:
        print("Encaixa")
    else:
        print("Não encaixa")


while(N > 0):
  valores = input().strip().split(" ")
  if len(valores) > 1:
    A, B = valores[0], valores[1]

    if (len(A) > 0 and len(B) > 0) and (len(A) <= 1000 and len(B) <= 1000):

      if A[len(A) - len(B):] == B:
        print("encaixa")
      else:
        print("nao encaixa")
      N -= 1 
  else:
    break



n = int(input())

while n > 0:
  
  values = input().split()

  
  aux = ''
  for digit in values[0][::-1]:
    aux += digit
    if aux == values[1][::-1]:
      print("encaixa")
      break
  else:
    print("nao encaixa")
  
  aux = ''
  
  n -= 1