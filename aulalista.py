# Leia uma string e escreva letra por letra 
string = input('Digite algo: ')
alfa = 'abcdefghijklmnopqrstuvwxyz'
for letras in string:
    for letra in alfa:
        if letras == letra[alfa]:
            print(letra)