# Leia uma string e escreva letra por letra versão feita pelo professor

texto = input('Qual seu nome?')
tam = len(texto)

indice = 0
while indice < tam:
    print(indice, texto[indice])
    indice += 1 