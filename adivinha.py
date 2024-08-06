# Escreva um programa de adivinhação de número. O programa deve conter um
#número secreto entre 1 e 1.000.000. O usuário deve chutar um número e o
#programa deve dizer se o número chutado é maior ou menor que o número secreto.
#O usuário deve tentar até acertar o número secreto. O código abaixo mostrar como
#sortear um número aleatório entre 0 e 10 em python:

import random

# Sorteia um número secreto entre 1 e 1.000.000
numero_secreto = random.randint(1, 1000000)

print("Adivinhe o número secreto entre 1 e 1.000.000")

while True:
    # Solicita ao usuário um chute
    tentativa = int(input("Digite seu palpite: "))
    
    # Compara a tentativa com o número secreto
    if tentativa < numero_secreto:
        print("O número secreto é maior.")
    elif tentativa > numero_secreto:
        print("O número secreto é menor.")
    else:
        print("Parabéns! Você acertou o número secreto!")
        break  # Sai do loop quando o número é acertado
