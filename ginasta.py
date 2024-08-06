#Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor
#e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça
#um programa em Python que receba o nome do(a) ginasta, e as notas de sua
#apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e
#a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e
#a pior nota para calcular a média). As notas não são informadas em ordem (crescente
#ou decrescente

ginasta = input('Informe o nome da atleta (ou digite "fim" para encerrar): ')

while ginasta != 'fim':
    j1 = float(input('Nota do jurado 1: '))
    j2 = float(input('Nota do jurado 2: '))
    j3 = float(input('Nota do jurado 3: '))
    j4 = float(input('Nota do jurado 4: '))
    j5 = float(input('Nota do jurado 5: '))
    j6 = float(input('Nota do jurado 6: '))
    j7 = float(input('Nota do jurado 7: '))

    melhor_nota = j1
    pior_nota = j1

    if j2 > melhor_nota:
        melhor_nota = j2
    if j3 > melhor_nota:
        melhor_nota = j3
    if j4 > melhor_nota:
        melhor_nota = j4
    if j5 > melhor_nota:
        melhor_nota = j5
    if j6 > melhor_nota:
        melhor_nota = j6
    if j7 > melhor_nota:
        melhor_nota = j7


    if j2 < pior_nota:
        pior_nota = j2
    if j3 < pior_nota:
        pior_nota = j3
    if j4 < pior_nota:
        pior_nota = j4
    if j5 < pior_nota:
        pior_nota = j5
    if j6 < pior_nota:
        pior_nota = j6
    if j7 < pior_nota:
        pior_nota = j7

    soma_notas = j1 + j2 + j3 + j4 + j5 + j6 + j7 - melhor_nota - pior_nota
    media = soma_notas / 5

    print(f'Atleta: {ginasta}')
    print(f'Melhor nota: {melhor_nota}')
    print(f'Pior nota: {pior_nota}')
    print(f'Média das notas (sem a melhor e a pior): {media:.2f}')
    
    ginasta = input('Informe o nome da atleta (ou digite "fim" para encerrar): ')
