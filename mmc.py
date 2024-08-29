def mmc(n1, n2):
  if n1 > n2:
    maior = n1
  else:
    maior = n2
  while True:
    if maior % n1 == 0 and maior % n2 ==0:
      print(maior)
      break
    else:
      maior += 1

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
(mmc(n1, n2))

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

(mdc(12, 18))