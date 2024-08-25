#Faça um programa em python que leia o nome de 4 times de futebol que estão em
#uma semifinal. Após, leia os gols das duas partidas: time 1 x time 2 e time 3 x time 4.
#Os times vencedores devem ir para a final. Caso haja empate, deve-se perguntar ao
#usuário qual time se classificou. Por fim, deve-se ler os gols da final e mostrar qual
#time foi campeão (se empatar, perguntar quem foi campeã

# Entradas para os nomes dos times
timeum = input('1º TIME: ')
timedois = input('2º TIME: ')
timetres = input('3º TIME: ')
timequatro = input('4º TIME: ')

# Fase semifinal
print('------ SEMIFINAL---------')
print(f'{timeum} X {timedois}')
goltimeum = int(input(f'Placar do {timeum}: '))
goltimedois = int(input(f'Placar do {timedois}: '))

print(f'{timetres} X {timequatro}')
goltimetres = int(input(f'Placar do {timetres}: '))
goltimequatro = int(input(f'Placar do {timequatro}: '))

# Determina os vencedores da semifinal
if goltimeum > goltimedois:
    finalista1 = timeum
else:
    finalista1 = timedois

if goltimetres > goltimequatro:
    finalista2 = timetres
else:
    finalista2 = timequatro

# Fase final
print('--- FINAL----')
print(f'{finalista1} X {finalista2}')
golfinalista1 = int(input(f'Placar do {finalista1}: '))
golfinalista2 = int(input(f'Placar do {finalista2}: '))

# Determina e imprime o vencedor do torneio
if golfinalista1 > golfinalista2:
    vencedor = finalista1
else:
    vencedor = finalista2

print(f'O campeão do torneio {vencedor}')