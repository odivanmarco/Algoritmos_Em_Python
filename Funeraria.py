# Primeira lista onde vai guardar todas as covas
cemiterio = []
# Inicializando variável option com 9, essa variável vai ser usada como varável de escolha no menu
option = 9
# Enquanto option diferente de 0, ele executa tudo que ta dentro do laço while
while True:
    print("\n♱♱♱♱♱ BEM VINDO A FUNERÁRIA VOCÊ É O PROXIMO ♱♱♱♱♱")
    print("         --> Digite 1 para ENTERRAR")
    print("         --> Digite 2 para ENCONTRAR UMA LÁPIDE")
    print("         --> Digite 3 para ALTERAR OS DADOS DO DIFUNTO")
    print("         --> Digite 4 para LISTAR")
    print("         --> Digite 0 para ENCERRAR")
    # Insere a opção númerica dentro da variavel option
    option = int(input("           Qual operação deseja efetuar?"))

    # Se option for igual a 1
    if option == 1:
        # Segunda lista, a lista cova, vai guardar informações sobre o difunto
        cova = []
        # Insere os dados via teclado
        quem_comprou = input("Nome de quem pagou o velório: ").upper()
        nome_difunto = input("Nome do difunto: ").upper()
        cor = input("Qual cor quer na lápide? ")
        frase = input("Qual frase quer na lápide? ")

        # adiciona as informações do difunto na lista cova, depois adiciona a lista cova, na lista cemitério
        cova.append(quem_comprou)
        cova.append(nome_difunto)
        cova.append(cor)
        cova.append(frase)
        cemiterio.append(cova)
    
    # Se option for igual a 2 procura um lápide específica
    elif option == 2:
        encontrou = False
        # A variavel pesquisa difunto, vai guardar o nome do difunto que vai pesquisar
        # Função upper deixa a letra maiuscula
        pesquisa_difunto = input("Qual nome do difunto que quer procurar?").upper()
        # Percorre a lista cemitério
        for i in cemiterio:
            # Verifica se pesquisa_difunto é igual a um elemento da lista
            if pesquisa_difunto == i[1]: 
                encontrou = True
                # Imprime as informações da cova
                print(f'\nO difunto {i[1]} está descansando em paz em uma de nossas lápides, \nGOSTA DE SE JUNTAR A ELE? BRINCADEIRINHA!!!')
                print(f'Nome na lápide {i[1]}')
                print(f'Cor da lápide: {i[2]}')
                print(f'Frase na lápide: {i[3]}\n')
        # Se a variavel encontrou continua falsa é porque não encontrou nenhum difunto com aquele nome
        if(encontrou == False):
            print("Esse difunto não consta em nosso cemitério!")
    
    # Se option for igual a 3 altera algumas informações
    elif option == 3:
        encontrou = False
        pesquisa_difunto = input("Qual nome do difunto que quer procurar para alterar?").upper()
        alteracao = int(input("O que seja alterar? 1 = FRASE NA LAPIDE, 2 = COR DA LÁPIDE : "))
        # Percorre o vetor cemiterio
        for i in cemiterio:
            if pesquisa_difunto == i[1]: 
                encontrou = True
                # Se for alterar a cor
                if alteracao == 2:    
                    i[2] = input("Qual cor você deseja para a lápide? ")
                # Se for alterar a frase
                elif alteracao == 1:
                    i[2] = input("Qual frase deseja colocar na lápide?")
        if(encontrou == False):
            print("Não foi possível alterar, este difunto não consta em nosso cemitério!")
            
    # Se option for igual a 4 imprime um relatório
    elif option == 4:
        print("♱♱♱♱♱♱♱♱♱♱♱♱♱ RELATÓRIO ♱♱♱♱♱♱♱♱♱♱♱♱♱")
        for i in cemiterio:
            # Na posicao 0 da lista dentro da lista cemiterio está o nome de quem pagou
            print(f'Nome de quem pagou: {i[0]}')
            # Na posicao 1 da lista dentro da lista cemiterio está o nome do difunto, e assim por diante
            # até a posição 3
            print(f'Nome do difunto: {i[1]}')
            print(f'Cor da lápide: {i[2]}')
            print(f'Frase na lápide: {i[3]}\n')

    # Se option for igual a 0 encerra o programa
    elif option == 0:
        print("TCHAU CLIENTE, TE DESEJO UMA BOA VIDA, LONGA NÃO !!! ")
        break
                


