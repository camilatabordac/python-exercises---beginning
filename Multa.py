#  Um radar de trânsito verifica a velocidade dos veículos.
#  Caso um veículo ultrapasse os 60km/h, emite-se um registro de multa.
#  O valor da multa é de R$200,00 mais R$3,00 para cada 1 km/h acima do limite. 
# Faça um programa em python que receba como entrada a velocidade do veículo e escreva na tela o valor da multa.

veiculo = float(input('Insira a velocidade do veículo: '))
velmax = 60
if veiculo > velmax:
    excesso =  veiculo - velmax 
    multa = 200 + ( 3 * excesso)
    print(f'Multa no valor de R${multa}')
else:
    print('Veículo na velocidade correta')