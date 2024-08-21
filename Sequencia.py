# Escreva um programa que leia diversos números até que o usuário digite zero. Em
#seguida escreva a média dos números digitados.

nao_e_zero = True
soma = 0
qtidade = 0
while nao_e_zero:
    num = int(input('Insira um número: '))
    soma += num
    qtidade += 1

    if num == 0:
        nao_e_zero = False
        media = soma / (qtidade - 1) 


print(media)

