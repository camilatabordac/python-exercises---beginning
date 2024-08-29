#Faça um programa que leia dois valores x e y, e calcula o valor de x
#dividido por y, além do resto da divisão. Não é permitido usar as
#operações de divisão e resto de divisão do Python (use apenas soma e
#subtração).
# Leitura dos valores x e y
x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

# Inicializando o quociente e o resto
quociente = 0
resto = x

# Loop para subtrair y de x até x ser menor que y
while resto >= y:
    resto -= y
    quociente += 1

# Exibindo os resultados
print(f"O quociente de {x} dividido por {y} é {quociente}")
print(f"O resto da divisão de {x} por {y} é {resto}")
