#Escreva um programa que mostre a seguinte sequência de números para um valor N informado pelo usuário:
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
#…
#N N N N N N N …

N = int(input('Insira um valor para a sequência da pirâmide'))
cont = 1 #vai controlar o número de linha
while cont <= N:
    # Imprime o número `cont` repetido `cont` vezes
    cont2 = 1 #responsavel por imprimir o num na mesma linha 
    while cont2 <= cont:
        print(cont, end=' ')
        cont2 += 1
    print()  # Para pular para a próxima linha
    cont += 1
