# Leia um nome e escreva apenas as vogais do nome - diga quantas vogais 
texto = input('Qual seu nome?')
tam = len(texto)

indice = 0
while indice < tam:
    letra = texto[indice]
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(texto[indice])
    indice += 1 