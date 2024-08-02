#Faça um programa em python que pergunte ao usuário o seguinte:
#a) A viagem custará menos de R$ 30?
#b) Terá Wifi?
#c) Terá piscina?
#d) Terá churrasqueira?
#O programa deverá mostrar se a viagem ocorrerá de acordo com as seguintes regras:
#- Deverá custar menos de R$ 30
#- Tem que ter wifi e piscina
#- Se não tiver wifi ou piscina, tem que ter churrasqueira


viagem = input("A viagem custará menos de R$30.00? (sim/não) ")
wifi = input('Terá wifi? (sim/não) ')
piscina = input("Terá piscina? (sim/não) ")
churras = input('Terá churrasqueira? (sim/não) ')

custar_menos_de_30 = viagem == 'sim'
ter_wifi = wifi == 'sim'
ter_piscina = piscina == 'sim'
ter_churrasqueira = churras == 'sim'

if viagem != 'sim':
    print('A viagem deve custar menos de R$30!')
    
if wifi == 'não' and piscina == 'não':
    if churras == 'não':
        print('Se não tiver wifi ou piscina, tem que ter churrasqueira.')

if custar_menos_de_30 and ter_wifi and ter_piscina:
    print('A viagem atenderá todas as condições necessárias!')
elif custar_menos_de_30 and (ter_wifi or ter_piscina or ter_churrasqueira):
    print('A viagem não atende a todos os requisitos.')
