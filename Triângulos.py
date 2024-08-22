a = int(input('Insira uma medida para o lado A:'))
b = int(input('Insira uma medida para o lado B:'))
c = int(input('Insira uma medida para o lado C:'))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo isósceles.")
    else:
        print("É um triângulo escaleno.")
else:
    print("As medidas informadas não podem formar um triângulo.")
