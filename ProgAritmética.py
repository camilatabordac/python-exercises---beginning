# Escreva um programa que calcule e mostre a soma dos números de 1 a N. Não utilize
# as equações de progressão aritmética.
n = int(input('Informe o valor de N:'))
soma = 0
cont = 1

while cont <= n:
    soma += cont  # Adiciona o valor atual de cont à soma
    cont += 1     # Incrementa cont para passar para o próximo número

print(f'A soma dos números de 1 até {n} é: {soma}')
