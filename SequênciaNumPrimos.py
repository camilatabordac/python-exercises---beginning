# Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os
#números primos contidos neste intervalo. Por exemplo, para x=3 e y=14 escreva:
#3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y

# Entrada dos valores x e y
x = int(input('Insira um valor para X: '))
y = int(input('Insira um valor para Y: '))

# Verifica se x é menor que y
if x >= y:
    print('O valor de X deve ser menor que Y')
else:
    # Inicia a verificação de números primos no intervalo [x, y]
    numero = x
    primeiro = True
    while numero <= y:
        # Verifica se o número atual é primo
        if numero >= 2:
            divisor = 2
            primo = True
            while divisor * divisor <= numero:
                if numero % divisor == 0:
                    primo = False
                    break
                divisor += 1

            # Se for primo, imprime o número
            if primo:
                if primeiro:
                    print(numero, end='')
                    primeiro = False
                else:
                    print(f', {numero}', end='')

        numero += 1

    # Quebra de linha ao final da impressão
    print()
