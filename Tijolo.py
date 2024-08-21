# Faça um programa em python que desenhe uma pirâmide conforme 2 dados
#informados pelo usuário. O primeiro dado indica o "tijolo" e o segundo a quantidade
#de andares.
#x: Informe o tijolo: A
#Informe a quantidade de andares: 5
#A
#AAA
#AAAAA
#AAAAAAA
#AAAAAAAAA

tijolo = input('Insira o que deseja ser o tijolo da escada: ')
andares =  int(input('Informe a quantidade de andares que deseja ter: '))
cont = 1 
while cont <= andares:
    cont1 = 1 
    while cont1 <= cont:
        print(tijolo, end=' ')
        cont1 += 1 
    print()
    cont += 1 





