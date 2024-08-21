#Escreva um programa que mostre a sequência de Fibonacci até o enésimo termo (n
#deve ser informado pelo usuário). A sequência de Fibonacci é aquela em que cada
#termo é a soma dos dois termos anteriores. Por exemplo, para n=8 escreva 0, 1, 1, 2,
#3, 5, 8 e 13.
n = int(input("Digite o valor de n: "))
a = 0
b = 1
count = 0
print("Sequência de Fibonacci:")
while count < n:
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b
    
    count += 1

