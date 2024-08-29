#Num certo país da América do Sul, a moeda nacional é a Merreca (M$). No sistema monetário
#desse país só existem cédulas de M$ 100, M$ 50, M$ 10, M$ 5 e M$ 1. Dado um valor em
#Merrecas, faça um script que retorne a quantidade mínima de cédulas que totalizam o valor
#especificado. Por exemplo, se o valor for M$ 379, devemos ter:
#3 cédulas de M$ 100
#1 cédula de M$ 50
#2 cédulas de M$ 10
#0 cédulas de M$ 5
#4 cédulas de M$ 1
valor = int(input('Entre com o valor em M$: '))
cedulas100 = valor // 100
resto = valor % 100
cedulas50 = resto // 50
resto = resto % 50
cedulas10 = resto // 10
resto = resto % 10
cedulas5 = resto // 5
resto = resto % 5
print('O valor digitado corresponde a:')
print('%d cédulas de M$ 100' %cedulas100)
print('%d cédulas de M$ 50' %cedulas50)
print('%d cédulas de M$ 10' %cedulas10)
print('%d cédulas de M$ 5' %cedulas5)
print('%d cédulas de M$ 1' %resto)