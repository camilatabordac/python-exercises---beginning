# Você vai perguntar o valor inicial investido na poupança, a rentabilidade mensal, quantos meses o cliente deseja 
# deixar o dinheiro investido e mostrar o valor final na conta do cliente do banco.
c = float(input("Digite o valor do capital a ser aplicado: "))
n = int(input("Digite a quantidade de meses da aplicação: "))
taxa = float(input("Informe a taxa de juros mensal: "))
i = taxa/100
m = c * ((1 + i)**n)
print("Após o investimento de R$ {:.2f} durante um período de {} meses a uma taxa de juros de {:.2f}% o valor a ser recebido será de R$ {:.2f}.".format(c, n, taxa, m))

# Um cliente pediu que o sistema do banco tivesse a seguinte função:
#Dizer o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha um valor 'vf', 
# supondo que este dinheiro esteja rendendo uma rentabilidade 'i' mensal, em porcentagem esse 'i'.

#Faça um programa que pede o valor final, o tanto de meses que vai ficar aplicado, 
# a rentabilidade e o script mostre o valor inicial que ele deve investir para atingir tal objetivo.
m = float(input("Informe o valor a ser obtido ao final do investimento: "))
n = int(input("Informe a quantidade de meses que você deseja investir: "))
taxa = float(input("Informe a taxa de juros mensal: "))
i = taxa/100
c = m / ((1 + i)**n)
print("Para se obter o valor final de R$ {:.2f} após {} meses de investimento a uma taxa de juros de {:.1f}%, você deverá fazer um investimento inicial de R$ {:.2f}.".format(m, n, taxa, c))