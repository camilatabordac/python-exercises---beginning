def escada():
  d = int(input("Sequencia de menores na escada, insira um numero:"))
  cont = d
  while cont > 0:
    soma = cont
    while soma > 0:
      print(soma, end=' ')
      soma -= 1
    print()
    cont -=1 

(escada())

def numeros(n):
    for c in range(1, n + 1):
        cont = 1
        while True:
            print(c, end=' ')
            if cont == c:
                break
            cont += 1
        print()
        
        
n = int(input('Digite um número: '))
numeros(n)