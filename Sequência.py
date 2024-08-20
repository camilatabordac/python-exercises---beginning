# Considere uma sequência de números que atende a todos critérios abaixo: a - Possui
#sempre 2 dígitos , nem mais , nem menos . b - A representação do número possui
#pelo menos um dígito 1 ou um dígito 2. c - O número é múltiplo de 3. Faça um
#programa que implemente e mostre essa sequência. obs: tem que usar repetição
#para mostrar a sequência. Não pode mostrar os números “na mão”
numero = 10  # Início com o menor número de dois dígitos

while numero < 100:  # Continua até o último número de dois dígitos
    # Extrai os dígitos do número
    dezena = numero // 10
    unidade = numero % 10

    # Verifica se o número contém o dígito 1 ou 2 e se é múltiplo de 3
    if (dezena == 1 or dezena == 2 or unidade == 1 or unidade == 2) and numero % 3 == 0:
        print(numero)

    numero += 1  # Incrementa para o próximo número
