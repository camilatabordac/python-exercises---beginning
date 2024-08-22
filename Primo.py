# Escreva um programa que receba um número inteiro positivo do usuário e verifique
# se ele é primo.

num = int(input('Insira um número inteiro positivo: '))
if num <= 1:
    print("Digite um número inteiro maior que 1!")
else:
    primo = True
    i = 2

    while i < num:
        if num % i == 0:
            primo = False
        i += 1
    
    if primo:
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo.")
