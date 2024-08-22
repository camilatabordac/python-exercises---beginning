#Construa um programa em Python que escreva uma contagem de 10 (dez) minutos,
#ou seja, mostre 0:00, e então 0:01, 0:02, ..., 0:58, 0:59, 1:00, 1:01, ..., até 10:00.

minuto = 0
segundo = 0

while minuto <= 10:
    print(f"{minuto}:{segundo}")
    segundo += 1
    if segundo == 60:
        minuto += 1
        segundo = 0
