#Exercício01
from random import randint

listaNum = []
entre10e20 = 0
pares = []
maior30 = 0
impares = []

for i in range(12):
    listaNum.append(randint(0,50))
print("\n-=-=-=-=-=-= Gerando os valores aleatórios =-=-=-=-=-=-\n")
print(f'Vetor aleatório gerado: {listaNum}')

for i in listaNum:
    if(i >10 and i <20):
        entre10e20+=1
    if(i % 2 == 0):
        pares.append(i)
    if(i>30):
        maior30+=1
    if(i %2 != 0):
        impares.append(i)

print(f'Quantidade de números entre 10 e 20: {entre10e20}')
print(f'Números pares: {pares}' )
print(f'Quantidade de números maiores que 30: {maior30}')
print(f'Numeros impares: {impares}' )


#Exercício02
lista10 = []
multiplos2 = []
multiplos5 = []
multiplos2e5 = []
print("\n=-=-=-=-=- Digite 10 valores inteiros -=-=-=-=-=\n")
for i in range(10):
    lista10.append(int(input(f'Digite o {i+1}º valor: ')))

for i in lista10:
    if(i % 2 == 0):
        multiplos2.append(i)
    if(i % 5 == 0):
        multiplos5.append(i)
    if(i % 2 == 0 and i % 5 == 0):
        multiplos2e5.append(i)

print(f'Números multiplos de 2:       {multiplos2} [total = {len(multiplos2)}]')
print(f'Números múltiplos de 5:       {multiplos5} [total = {len(multiplos5)}]')
print(f'Números múltiplos de 2 e 5:   {multiplos2e5} [total = {len(multiplos2e5)}]')
