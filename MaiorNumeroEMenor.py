numeros = []
maior = 0
menor = 99999999999999
for i in range(12):
    numeros.append(int(input(f'Digite o {i+1}º número: ')))

for i in range(12):
    if(numeros[i] > maior):
        maior = numeros[i]
        posicaoMaior = i

    if(numeros[i] < menor):
        menor = numeros[i]
        posicaoMenor = i

print(f'Maior elemento: {maior}')
print(f'Posição no vetor: {posicaoMaior}\n')

print(f'Menor elemento: {menor}')
print(f'Posição no vetor: {posicaoMenor}')
