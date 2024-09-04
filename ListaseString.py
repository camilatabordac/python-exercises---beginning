# Faça o usuário digitar uma lista de compras e que pare quando ele pedir

ListCompras = []
Compras = ' ' #Haverá algo que o usuário estará digitando 

while Compras != '' : #Enquanto o usuário não digitar um espaço vazio
    Compras = input("Digite os itens para a sua lista de compras: ")
    ListCompras.append(Compras) #Metodo para adicionar os itens as listas 


i = 0 
while i < len(ListCompras): #enquanto contador for menor que o tamanho da lista
    print(ListCompras[i]) #Printa cada indice
    i += 1 
