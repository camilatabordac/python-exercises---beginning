 #Crie um programa em Python que leia uma data inicial e um número de dias. 
 # Calcule e escreva a data correspondente ao número de dias. 

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

diascontados = int(input('Número de dias: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: #contabilizo os dias no mes que tem 30 dias
    dias_no_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_no_mes = 30

cont = 0

while diascontados > 0: # enquanto os dias digitados forem maior que zero
    if dia + diascontados <= dias_no_mes:#se o dia da data atual mais os dias que devem ser contador forem menor que 30
        dia = dia + diascontados # dia recebe dia mais os dias para contagem 
        diascontados = 0 # dias contados são igualados a zero porquem foram adicionados ao mês 
    else: # se ultrapassa os dias do mês 
        diascontados = diascontados - (dias_no_mes - dia + 1) 
        dia = 1
        mes = mes + 1 
        if mes > 12:
            mes = 1
            ano = ano + 1


# Exibe a data final
print(f"A nova data é: {dia:02d}/{mes:02d}/{ano}")