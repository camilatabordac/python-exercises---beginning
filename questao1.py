largura = int(input("Insira a largura da figura geométrica: "))
comprimento = int(input("Insira o comprimento da figura geométrica: "))

if largura <= 0 or comprimento <= 0:
    print('Erro: A largura e o comprimento devem ser maiores que zero.')
elif largura == comprimento:
    print("É um quadrado")
else:
    print('É um retângulo')
