#Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que
#o nome de um funcionário seja “fim”. Em seguida escreva:
#a) O nome do funcionário com maior salário
#b) O nome do funcionário com menor salário
#c) A média dos salários digitados

print('-Seja Bem-Vindo!')

maior_salario = -1
menor_salario = 0
soma_salarios = 0
quantidade_funcionarios = 0
nome_maior_salario = ""
nome_menor_salario = ""
nome = input('Insira o nome do funcionário (ou "fim" para encerrar): ')
while nome != 'fim':
    salario = float(input('Insira o salário referente: '))
    
    if salario > maior_salario:
        maior_salario = salario
        nome_maior_salario = nome
    
    if salario < menor_salario:
        menor_salario = salario
        nome_menor_salario = nome
    
    soma_salarios += salario
    quantidade_funcionarios += 1
    
    nome = input('Insira o nome do próximo funcionário (ou "fim" para encerrar): ')

if quantidade_funcionarios > 0:
    media_salarios = soma_salarios / quantidade_funcionarios
    print(f'O nome do funcionário com maior salário: {nome_maior_salario}')
    print(f'O nome do funcionário com menor salário: {nome_menor_salario}')
    print(f'A média dos salários digitados: {media_salarios:.2f}')
else:
    print('Nenhum salário foi digitado.')
