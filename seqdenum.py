#Considere uma sequência de números que atende a todos critérios abaixo: a - Possui
#sempre 2 dígitos , nem mais , nem menos . b - A representação do número possui
#pelo menos um dígito 1 ou um dígito 2. c - O número é múltiplo de 3. Faça um
#programa que implemente e mostre essa sequência. obs: tem que usar repetição
#para mostrar a sequência. Não pode mostrar os números “na mão”.

num = 10  # Começa com o menor número de dois dígitos

while num < 100:
    unidade = num % 10  # Obtém o dígito das unidades
    dezena = num // 10  # Obtém o dígito das dezenas
    
    # Verifica se o número é múltiplo de 3 e se possui pelo menos um dígito 1 ou 2
    if (num % 3 == 0) and (unidade == 1 or unidade == 2 or dezena == 1 or dezena == 2):
        print(num)
    
    num += 1  # Passa para o próximo número
