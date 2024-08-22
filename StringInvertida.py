#Leia uma palavra e mostre seu espelho do nome Exemplo: Camila Taborda ficará Alimac Adrobat
nome = input('Digite seu nome completo:')
nomeinvertido = ''

for letra in nome:
    nomeinvertido = letra + nome
    print(nomeinvertido)


