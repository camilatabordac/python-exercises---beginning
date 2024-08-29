
#Crie um programa em Python que solicite ao usuário um número inteiro positivo. 
# O programa deve dividir esse número sucessivamente por 2 até que o resultado seja menor que 1. 
# Em cada divisão, o programa deve exibir o resultado da divisão. 
# Ao chegar a um resultado menor que 1, o programa deve exibir a mensagem "Chegou a zero!".

num = int(input('Informe um número: '))
if num < 0:
    print('Deve ser inteiro positivo!')
else:
    resultado = num / 2
    print(f'O resultado da divisão é {resultado}')
    while resultado > 1:
        resultado = resultado / 2 
        print(f'O resultado da divisão é {resultado}')

