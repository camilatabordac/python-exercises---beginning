#Escreva um programa que calcule o fatorial de um número fornecido pelo usuário. O
#fatorial de um número n é o produto de todos os números inteiros de 1 a n.

print('Fatorial')
n = int(input('Insira o valor de N: '))
cont = 1 # começa em um pra obter o produto dos numeros inteiros de 1 a n
acum = 1 # acumular os numeros

while cont <= n:
    acum *= cont
    cont += 1

print(f'O fatorial do número {n} é {acum}')

