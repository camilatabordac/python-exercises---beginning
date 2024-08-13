nota1 = int(input('Insira a nota do 1º Bimestre: '))
nota2 = int(input('Insira a nota do 2º Bimestre: '))
nota3 = int(input('Insira a nota do 3º Bimestre: '))
nota4 = int(input('Insira a nota do 4º Bimestre: '))
freq = int(input('Insira sua frequência (em %): '))


media = (nota1 + nota2 + nota3 + nota4) / 4

if freq < 75:
    print('Reprovado por falta')
elif media < 3:
    print('Reprovado por nota')
elif media >= 7:
    print('Aprovado por média')
else:
    print('Ficou em exame')
