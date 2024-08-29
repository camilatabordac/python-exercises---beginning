#Foi feita uma pesquisa entre os habitantes de uma região. 
# Foram coletados os dados de idade, sexo (M/F) e salário. 
#Faça um programa que solicite esses dados 
#(finalize a entrada de dados ao ser digitada uma idade negativa) 
#e mostre:
#a) A média dos salários do grupo;
#b) A maior e a menor idade do grupo;
#c) A quantidade de mulheres na região;
#d) A idade e o sexo da pessoa que possui o maior salário;

media_sal = 0
total_sal = 0 
cont_pessoas = 0
maior_idade = 0
menor_idade = 200
num_mulheres = 0
idade_rico = 0
idade = 0
maior_sal = 0
  
while idade >= 0:
    idade = int(input("Digite a idade: "))
    if (idade >= 0):
        sexo = input("Digite o sexo: ")
        salario = float(input("Digite o salário: "))
        
        total_sal = total_sal + salario
        cont_pessoas = cont_pessoas + 1
        
        if idade > maior_idade:
            maior_idade = idade
        
        if idade < menor_idade:
            menor_idade = idade
        
        if sexo == "F":
            num_mulheres = num_mulheres + 1  
        
        if salario > maior_sal:
            maior_sal = salario
            sexo_rico = sexo
            idade_rico = idade
    
        if cont_pessoas == 0:
            print("Pessoas insuficientes para pesquisa")
        else:
            media_sal = total_sal / cont_pessoas
        
        print("média dos salários: ",media_sal)
        print("Maior e menor idade: ",maior_idade,menor_idade)
        print("Quantidade de mulheres: ", num_mulheres)
        print("Idade e o sexo do maior salário: ",idade_rico,sexo_rico)