# Crie um programa que leia os dois lados de um retângulo e escreva a sua área.
#  Verifique para que o usuário digite apenas números positivos para representar
#  os lados.

base = int(input('Insira a largura: '))
altura = int(input('Insira o comprimento: '))

área = base * altura
if base < 0 or altura < 0:
    print('Apenas números positivos!')
else:
    print(f'Sua área é {área}.')