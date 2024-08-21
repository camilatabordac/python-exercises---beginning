#Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n
#deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada
#termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2,
#3, 5, 8 e 13.
n = int(input("Digite o valor de n: "))
fib1 = 0
fib = 1
cont = 0
print("Sequência de Fibonacci:")
while cont < n:
    print(fib1, end=" ")
    fib2 = fib1 #armazendo a em uma variavel temporaria
    fib1 = fib #a vai receber o valor b
    fib = fib2 + fib # b vai receber o valor da variavel temporaria mais b
    cont += 1

