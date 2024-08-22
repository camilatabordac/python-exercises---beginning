#Leia uma musica uma vogal alvo, escreva a música trocando todas as vogais pela vogal alvo versão prof

texto = input('Digite: ')
alvo = input('Digite: ')
saida = ''
tam = len(texto)
ind = 0

while ind < tam:
    letra = texto[ind]
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        saida += alvo
    else:
        saida += letra
    
    ind += 1

print(texto)
print(saida)