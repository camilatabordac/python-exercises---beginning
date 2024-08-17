# Leia um nome e escreva apenas as vogais do nome - diga quantas vogais 
texto = input('Qual seu nome?')
tam = len(texto)
vogais = ''
indice = 0
num_vogais = 0
while indice < tam:
    letra = texto[indice]
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        vogais = vogais + letra #concatenando 
        num_vogais = num_vogais +1
    indice += 1 

print(f'vogais, num_vogais, {100*num_vogais/tam}%')