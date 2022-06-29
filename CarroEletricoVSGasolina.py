
while True:
    option = input("Digite s para calcular ou digite n para parar o programa\n Opção:")
    if(option == 's'):
        km_porKW = float(input("Quantos KWh possui seu veículo?"))
        km_ref = float(input("Quantos km você quer como referência?"))
        km_max = float(input("Quantos km máximo sua bateria aguenta?"))

        resultado = (km_porKW * km_ref) / km_max
        gasto = resultado * 0.50 
        print(f'Serão gastos: {resultado:.2f} a cada {km_ref:.2f}Km')
        print(f'O que implica que você gastaria: {gasto:.2f} com o carro elétrico em {km_ref:.1f}KM e com um carro a gasolina seria {gasto * 6:.2f}')
    elif(option == 'n'):
        print("Saindo!!!")
        break
    else:
        print("Digite apenas s ou n!")


