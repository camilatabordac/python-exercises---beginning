#Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n
#deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada
#termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2,
#3, 5, 8 e 13.

# Solicita ao usuário o número de termos desejado
n = int(input("Digite o valor de n: "))

# Inicializa os dois primeiros termos da sequência de Fibonacci
a, b = 0, 1
count = 0  # Contador para controlar o número de termos exibidos

print("Sequência de Fibonacci:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
