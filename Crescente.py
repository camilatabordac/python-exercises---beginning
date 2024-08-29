# Faça um programa em python que leia 3 números e os mostre em ordem crescente
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Comparação e troca dos números para ordenação
if num2 < num1:
    num1, num2 = num2, num1

if num3 < num2:
    num2, num3 = num3, num2

if num2 < num1:
    num1, num2 = num2, num1

# Exibição dos números em ordem crescente
print("Números em ordem crescente:", num1, num2, num3)
