#Faça um programa, em Python, que leia vários endereços IP (Internet Protocol
#address, ou Endereço de Protocolo da Internet). A partir dos IPs lidos mostre se são
#endereços IP válidos ou inválidos. O formato de um endereço IP é
#num1.num2.num3.num4 (pode ler cada número separado), onde 1 ≤ num1 ≤ 255,
#0 ≤ num2 ≤ 255, 0 ≤ num3 ≤ 255 e 0 ≤ num4 ≤ 255
print('IP é um conjunto de  4 números, no entanto existem algumas regras para serem válidos ou não.')
print('Me informe os 4 conjuntos separadamente para ao final te informar se é válido ou não!')
parar = 0
while parar == 0:
  n1 = int(input('Digite o primeiro conjunto:'))
  n2 = int(input('Digite o segundo conjunto:'))
  n3 = int(input('Digite o terceiro conjunto:'))
  n4 = int(input('Digite o quarto conjunto:'))
  if n1 < 1 or n1 > 255:
    print('IP inválido')
  else: 
    if n2 < 1 or n2 > 255:
      print('IP inválido')
    else:
      if  n3 < 1 or n3 > 255:
         print('IP inválido')
      else: 
         if n4 < 1 or n4 > 255:
            print('IP inválido')
         else:
           print(f'IP válido {n1}.{n2}.{n3}.{n4}')

    


  parar = float(input('Se deseja continuar digite "0"; Se deseja encerrar digite um número maior do que 0: '))