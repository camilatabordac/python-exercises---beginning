


def ppt():
  nome1 = input('Qual o nome do primeiro jogador? ')
  nome2 = input('Qual o nome do segundo jogador? ')

  player1 = 0
  player2 = 0

  interromper = 1
  interromperp1 = 1
  interromperp2 = 1
 

  while interromper != 0:

    #Fazendo os jogadores escolherem dentro de "whiles", pra perguntar de novo se for necessário:
    while interromperp1 == 1:
      player1 = (input(f'{nome1}, digite "pedra", "papel" ou "tesoura": '))
  
      if player1 != "pedra" and player1 != "papel" and player1 != "tesoura":
        #Se esse jogador escolher algo errado, eu faço o programa perguntar de novo:
        print('Escolha inválida, digite de novo e atente-se aos erros!')
      else:
        #Se ele escolher algo certo, faço o while parar:
        interromperp1 = 0
        
    while interromperp2 == 1:
      player2 = (input(f'{nome2}, digite "pedra", "papel" ou "tesoura": '))

      if player2 != "pedra" and player2 != "papel" and player2 != "tesoura":
        #Mesmo processo aqui, se estiver errado repete:
        print('Escolha inválida, digite de novo e atente-se aos erros!')
      else:
        #Se estiver certo, para a repetição e continua com o programa
        interromperp2 = 0

    #Testando quem ganhou:
    if player1 == player2:
      #Se empatar vai ter que rodar o código de novo! Por que? Porque to com preguiça de fazer repetir só o "pedra, papel ou tesoura" ;)
      print(f'Empatou! Tentem de novo.')
      #Mudo o interromper para parar com o "while principal":
      interromper = 0
      
    else: 
      #Aqui deu uma caralhada de "if's", mas finge que tem pouco:
      if player1 == "pedra" and player2 == "tesoura":
        print(f'O {nome1} ganhou!')
        interromper = 0
      else:
        if player2 == "pedra" and player1 == "tesoura": 
          print(f'O {nome2} ganhou!')
          interromper = 0
        else:
          if player1 == "tesoura" and player2 == "papel":
            print(f'O {nome1} ganhou!')
            interromper = 0
          else:
            if player2 == "tesoura" and player1 == "papel":
              print(f'O {nome2} ganhou!')
              interromper = 0
            else:
              if player1 == "papel" and player2 == "pedra":
                print(f'O {nome1} ganhou!')
                interromper = 0
              else:
                if player2 == "papel" and player1 == "pedra":
                  print(f'O {nome2} ganhou!')
                  interromper = 0

      interromper = 0

ppt()
  