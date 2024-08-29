#Imagine que em uma disciplina a nota final é obtida da seguinte forma: trabalho tem peso 25% e a prova tem peso 75%.
#  Faça um algoritmo que calcule a nota final desta disciplina. Se a nota for inferior a 7,0
# o algoritmo deve apresentar a mensagem “Está em exame.”. 
# Caso contrário, deve apresentar a mensagem: “Aprovado com a nota X”.")

trabalho = int(input("Insira a nota do trabalho:"))
prova = int(input("Insira a nota da prova:"))
pesotrabalho = 25 / 100
pesoprova = 75 / 100
notatrabalho = trabalho * pesotrabalho
notaprova = prova * pesoprova
final = notatrabalho + notaprova
if final > 7:
  print("Aprovado com", final)
if final < 7:
  print("Reprovado com", final)