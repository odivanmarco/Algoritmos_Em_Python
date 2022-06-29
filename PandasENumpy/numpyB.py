import numpyB as np
#É possivel fazer a declaração de um array com numpy e já seta os valores no array, o array pode ser X diensional
#Abaixo temos dois exemplos, um unidimensional e um bidimensional
array_unidimensional = np.array([1,2,3,4,5,6,7,8,9,10])
print(f'Array unidemensional: \n{array_unidimensional}')
array_bidimensional = np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print(f'Array bidimensional: \n{array_bidimensional}')


#É possivel fazer alteração das dimensões em um array, vamos realizar no array unidimensional
#Vamos transformar o array unidimensional em um array com 5 linhas e 2 colunas
array_unidimensional = array_unidimensional.reshape(5,2)
print(f'Array unidimensional depois do redimensionamento: \n {array_unidimensional}')
#Agora o array bidimensional em um array com 1 linhas 10 colunas
array_bidimensional = array_bidimensional.reshape(1,10)
print(f'Array didimensional depois do redimensionamento: \n {array_bidimensional}')


#Criando um array totalmente preechido por zeros
array_zeros = np.zeros(10 , dtype=int)
print(f'Array preenchido com zeros: \n{array_zeros}')
#Ou criando um array com 5 linhas, 2 colunas e preenchendo com numeros uns
array_uns = np.ones((5,2), dtype=int)
print(f'Array de uns com 5 linhas e 2 colunas \n{array_uns}')

#É possivel se criar arrays com valores sequencias com a seguinte função
array_sequencial = np.arange(10)
print(f'Array sequencial: \n{array_sequencial}')
#Pode se combinar a função arange com a função vista anteriormente(reshape)
array_sequencial2 = np.arange(10).reshape(2,5)
print(f'Array com arange e reshape: \n{array_sequencial2}')

#Pode-se também fazer operações aritméticas com esses arrays
#No exemplo abaixo, estamos somando, subtraindo, multiplicando e dividindo todo o array
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
soma = a + b # Soma
subtracao = a - b # Subtração
multiplicacao = a * b # Multiplicação
divisao = a / b # Divisão
print('Soma = \n', + soma)
print('\n')
print('Subtração = \n', + subtracao)
print('\n')
print('Multiplicação = \n', + multiplicacao)
print('\n')
print('Divisão = \n', + divisao)

#Com o numpy também se consegue preencher um array, com valores com determinado intervalo
print("\nArray com númenos multiplos de 3 de 0 a 30: ")
a = np.arange(0,31,3)
print(a)
print("\nArray com númenos multiplos de 2 de 100 a 0: ")
b = np.arange(100,-1,-2)
print(b)

# Também é possível concatenar arrays de mesma dimensão
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
d = np.concatenate((a,b,c))
print(f"Arrays concatenados: {d}")

#Para saber algumas informações sobre os arrays temos as seguintes funções
a = np.array([1,2,3])
b = np.array([[4,5,6],[7,8,9]])
c = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]], [[0, 1, 2, 3], [4, 5, 6, 7]], [[0 ,1 ,2, 3], [4, 5, 6, 7]]])
print(f"\nTamanho dos array em dimensões: \nArray a : {a.ndim}\nArray b: {b.ndim} \nArray c: {c.ndim}" )
print(f'\nTamanho dos array: \nArray a : {a.size}\nArray b: {b.size} \nArray c: {c.size}')
print(f'\nForma do array (shape): \nArray a : {a.shape}\nArray b: {b.shape} \nArray c: {c.shape}')

#Indexação e fatiamento
data = np.array([1, 2, 3])
print("indexação e fatiamento")
print(data[1:])
print(data[-3:])
print(data[0])
print(data[0:2])

#Condições na hora de imprimir os arrays
a = np.arange(0,101,3)
print(a[a % 5 == 0])
print(a[a % 2 == 0])
