senha = input("Para acessar, digite sua senha: ")
gabarito = 'bob'
tentativas = 5
while senha != gabarito and tentativas > 0:
 		senha = input("Senha incorreta. Tente novamente: ")
 		tentativas = tentativas - 1 
 	
 
if senha == gabarito: 
	print('senha correta')
else:
	print('Limite de tentativas atingido')
