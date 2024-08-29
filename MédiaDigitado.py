#Escreva um programa que leia diversos números até que o usuário digite zero. 
# Em seguida escreva a média dos números digitados

num = int(input('Insira um número:'))
media = 0
quantidadedenum = 0
somanum = 0
while num != 0:
  num = int(input('Insira um número:'))
  quantidadedenum += 1
  somanum += num
  if num != 0:
    media = somanum // quantidadedenum

print('A media dos números é :', media)
