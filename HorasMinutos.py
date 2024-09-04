#Escreva um programa em python que leia o horário (horas e minutos) de partida de um voo, o tempo de viagem
#  e a diferença em horas do fuso horário do destino. O programa deve informar qual será o horário local no 
# destino previsto para a chegada do voo. Lembrando que o voo pode chegar no dia seguinte.
#Ex:
#Informe o horário de partida (horas): 14
#Informe o horário de partida (minutos): 00
#Informe o tempo de viagem (horas): 1
#Informe o tempo de viagem (minutos): 30
#Informe o fuso horário (horas): 3
#O horário previsto para chegada no destino é: 18:30

horas = int(input('Insira a hora de partida do vôo: '))
minutos = int(input('Insira os minutos de partida do vôo: '))
tempoviagemh = int(input('Insira o tempo de viagem do vôo em horas : '))
tempoviagemmin = int(input('Insira o tempo de viagem do vôo em minutos : '))
Fuso = int(input('Insira o fuso de viagem do lugar de destino: '))

final = hora_ini + tempo_h + fuso_h
min_final = min_ini + tempo_min
  
h_final = h_final + (min_final // 60)
min_final = min_final % 60
  
h_final = h_final % 24
  
print("hora final: ",h_final,":",min_final)

