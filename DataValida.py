dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_valida = False
dias_no_mes = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_no_mes = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_no_mes = 30
elif mes == 2:
    dias_no_mes = 28
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_no_mes = 29
        
if 1 <= mes <= 12 and 1 <= dia <= dias_no_mes:
    data_valida = True

if data_valida:
    print("A data é válida.")
else:
    print("A data é inválida.")
