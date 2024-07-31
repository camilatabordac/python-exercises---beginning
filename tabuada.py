num = int(input("Insira o número da tabuada:" ))
cont = 0 
while cont <= 10:
	produto = num * cont
	print(f"{cont} X {num} = {produto}")
	cont += 1
