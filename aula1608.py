x = 'Davi'
F = x[1] + 'u' + x[2] + x[3]
print(F)

nome = x + ' ' + 'vieira'
print(nome)

# Leia uma string e escreva letra por letra 
# Leia um nome e escreva apenas as vogais do nome - diga quantas vogais 
#Leia uma palavra e mostre seu espelho

nome = input('Qual seu nome?')
vogais = ['a', 'e', 'i', 'o', 'u']
tamnome = len(nome) # variavel pra somar a string nome
cont = 0 # somar a qtd de vogais
for vogal in vogais: # para cada vogal na lista vogais
    for letras in range(tamnome): # para letra que estiver percorrendo a string do nome
        if vogal == nome[letras]:  # se a vogal for igual a letra que percorreu na string do nome
            cont += 1 
            print(cont)
            print(vogal)
        

print(f'O nome {nome} tem {cont} vogais e são elas {vogal}.')
