# Crie um programa em Python que leia um número inteiro entre 1000 e 9999 e escreva o número com os dígitos invertidos. 
num = int (input('Digite um número entre 1000 e 9999: '))
if num < 1000 or num > 9999:
    print('Entre 1000 e 9999!')

milhar = num // 1000 
centena = (num // 100) % 10
dezena = ( num // 10 ) % 10
uni = (num // 1 ) % 10

print(f'O número invertido é {uni}{dezena}{centena}{milhar}')
