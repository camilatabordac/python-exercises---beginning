def fabrica():
  pequeno = int(input('Insira a quantidade de bermudas pequenas arrecadadas:'))
  medio = int(input('Insira a quantidade de bermudas médias arrecadadas:'))
  grande = int(input('Insira a quantidade de bermudas grandes arrecadadas:'))
  extrag = int(input('Insira a quantidade de bermudas extra grandes arrecadadas:'))
  p = pequeno * 8
  m = medio * 10
  g = grande * 14
  xg = extrag * 18
  vt = p + m + g + xg
  print('O valor total arrecadado foi de R$', vt)

(fabrica()) 