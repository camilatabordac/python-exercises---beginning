#Programa que imprime a soma de todos os números
#pares entre dois números quaisquer, incluindo-os

def somapar(n1, n2):
  soma = 0
  for n in range(n1 , n2 + 1):
    if n % 2 == 0:
      soma += n
  return(soma)
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
(somapar(n1, n2))