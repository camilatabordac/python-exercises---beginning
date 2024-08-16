#Leia uma musica uma vogal alvo, escreva a música trocando todas as vogais pela vogal alvo

musica = input('Digite a música:')
alvo = 'A'
vogais = ['E', 'I', 'O', 'U']
mustrocada = ''
for letras in musica:
    if letras in vogais:
        mustrocada += alvo
    else: 
        mustrocada += letras


print(mustrocada)