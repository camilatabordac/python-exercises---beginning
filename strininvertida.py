string = input('Digite algo: ')
stringinvertida = ''
ultimoindice = len(string) - 1 #pra pegar a ultima letra da palavra 

while ultimoindice >= 0: #percorrer de tras pra frente os indices 
    stringinvertida += string[ultimoindice] #pega a ultima letra da string original e concatena na string invertida
    ultimoindice -= 1 #todos os caracteres vao ser percorridos de tras pra frente 

print(stringinvertida)