from random import randint

valores = ('pedra','papel','tesoura')
while True:
    print('<--------- Pedra Papel Tesoura --------->')

    computador = randint(0,2)
    jogador = int(input("\n0 = pedra, 1= papel, 2 = tesoura -1 para sair: "))
    if(jogador == -1):
        print('Saindo!!!')
        break
    elif(jogador <0 or jogador >2 ):
        print('\nOpção inválida! Vamos tentar novamente')
    else:
        print(f'O computador lançou: {valores[computador]} ')
        print(f'O jogador lançou: {valores[jogador]} ')
        if computador == 0:
            if jogador == 0:
                print('EMPATE')
            elif jogador == 1:
                print('JOGADOR VENCEU')        
            elif jogador == 2:
                print('COMPUTADOR VENCEU')

        elif computador == 1:
            if jogador == 0:
                print('COMPUTADOR VENCEU')
            elif jogador == 1:
                print('EMPATE')
            elif jogador == 2:
                print('JOGADOR VENCEU')     
        
        elif computador == 2:
            if jogador == 0:
                print('JOGADOR VENCEU')  
            elif jogador == 1:
                print('COMPUTADOR VENCEU')
            elif jogador == 2:
                print('EMPATE')
    
