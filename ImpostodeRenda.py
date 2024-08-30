#Crie um programa em Python que leia o rendimento mensal do usuário, qual o
#modelo de imposto (sem correção/com correção das perdas no governo Bolsonaro) e
#retorne o quanto ele deve pagar de imposto
rendimento_mensal = float(input("Digite o seu rendimento mensal: "))
modelo = int(input("Escolha o modelo de imposto (1 para sem correção / 2 para com correção): "))

if modelo == 1:  # Sem correção das perdas no governo Bolsonaro
    if rendimento_mensal <= 1903.98:
        imposto_a_pagar = 0
    elif rendimento_mensal <= 2826.65:
        imposto_a_pagar = rendimento_mensal * 0.075 - 142.80
    elif rendimento_mensal <= 3751.05:
        imposto_a_pagar = rendimento_mensal * 0.15 - 354.80
    elif rendimento_mensal <= 4664.68:
        imposto_a_pagar = rendimento_mensal * 0.225 - 636.13
    else:
        imposto_a_pagar = rendimento_mensal * 0.275 - 869.36

elif modelo == 2:  # Com correção das perdas no governo Bolsonaro
    if rendimento_mensal <= 2500.00:
        imposto_a_pagar = 0
    elif rendimento_mensal <= 3200.00:
        imposto_a_pagar = rendimento_mensal * 0.075 - 187.50
    elif rendimento_mensal <= 4250.00:
        imposto_a_pagar = rendimento_mensal * 0.15 - 480.00
    elif rendimento_mensal <= 5300.00:
        imposto_a_pagar = rendimento_mensal * 0.225 - 826.25
    else:
        imposto_a_pagar = rendimento_mensal * 0.275 - 1074.50

else:
    print("Modelo de imposto inválido.")
    imposto_a_pagar = None

if imposto_a_pagar is not None:
    print(f"Você deve pagar R$ {imposto_a_pagar:.2f} de imposto.")
