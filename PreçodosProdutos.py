#Quanoo perguntar o item, perguntar também o preço do produto.
#Fazendo duas listas, uma com os itens e outra com o preço

item = []
preçositens = []
Compras = ' '
while Compras != '' : #Enquanto o usuário não digitar um espaço vazio
    Compras = input("Digite os itens para a sua lista de compras: ")
    Preços = int(input('Digite os preços do produto correspondente: '))
    item.append(Compras) #Metodo para adicionar os itens as listas
    preçositens.append(Preços)
i = 0 
while i < len(item): #enquanto contador for menor que o tamanho da lista
    i += 1 

c = 0
while c < len(preçositens):
    c += 1 

print(f'Item: {item[i]} Preços{preçositens[c]}')