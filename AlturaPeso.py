#A partir da altura, do sexo e do peso informados pelo usuário, construa um algoritmo que calcule o peso
#ideal e a variação (em valor absoluto e percentual). Após, informe se a pessoa está com peso elevado, normal
#ou inferior, levando-se em consideração o peso normal como uma variação de 8% para mais ou para menos.
#Utilize as seguintes fórmulas:
#a) para homens: (72,7 * h) – 58
#b) para mulheres: (62.1 * h) – 44.7

altura = int(input("Informe a altura em cm:"))
sexo = int(input("Informe seu sexo, digitando 1 para feminino e 0 para masculino:"))
peso = int(input("Informe seu peso em kg:"))
if sexo == 0:
  pesoideal = (72,7 * altura) - 58 * 0,8
if sexo == 1:
  pesoideal =  (62.1 * altura) - 44.7

var = pesoideal * 0.8
peso1 = pesoideal - var
peso2 = pesoideal + var

if pesoideal < peso2:
  print("Acima")
else:
  if pesoideal < peso1:
    print("Abaixo")
  else:
    print("Normal")