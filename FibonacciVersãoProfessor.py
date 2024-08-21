n = int(input("Digite o valor de n: "))
fib1 = 1
fib2 = 0
fib = 0
cont = 3
print(f"1º -> {fib2}")
print(f"2º -> {fib1}")
while cont <= n:
    fib  = fib2 + fib1
    print(f'{cont}º -> {fib}')
    cont += 1 
    fib2 = fib1
    fib1 = fib
