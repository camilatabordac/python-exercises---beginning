# Faça um programa em python que leia um valor inteiro X. 
# Em seguida apresente os 6 valores ímpares consecutivos a partir de X, inclusive o X se for o caso. 
# Por exemplo, para o número 8, a saída será “9,11,13,15,17,19”.

valor = int(input("Insira um número:"))
cont  = 0
while cont < 6:
  if valor % 2 != 0:
    print(valor, end=' - ')
    cont += 1
  valor += 1