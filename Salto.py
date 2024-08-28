# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
# No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
# O seu resultado fica sendo a média dos três valores restantes. 
# Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
# e depois informe a média dos saltos conforme a descrição acima informada 
# (retirar o melhor e o pior salto e depois calcular a média). 
# Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, 
# portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. 
# A saída do programa deve ser conforme o exemplo abaixo:

colocado = 'Primeiro','Segundo','Terceiro','Quarto','Quinto'

melhor_salto = pior_salto = contagem = media_saltos = total_saltos = media= 0

atleta = ' '

while atleta != '':

   atleta = input("Atleta: ")

   if atleta == '':

       break

   for c in range(0, 5):

       salto = float(input(f"{colocado[c]} salto: "))

       contagem += 1

       media_saltos += 1

       if salto > melhor_salto:

           melhor_salto = salto

       if salto < pior_salto or contagem == 1:

           pior_salto = salto

       total_saltos += salto

       media = total_saltos / media_saltos

print("="*25)

print(f"Melhor salto: {melhor_salto}")

print(f"Pior salto: {pior_salto}")