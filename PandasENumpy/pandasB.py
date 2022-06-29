import pandas as pd

print('################################')
print('Exemplo 1\n')
# Transformando um dicionário em dataFrame
alunos = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
                'Nota': [4, 7, 5.5, 9],
                'Aprovado': ['Não', 'Sim', 'Não','Sim']}

alunos_df = pd.DataFrame(alunos) #Comando que transforma o dict em DataFrame
print(alunos_df)

print('################################')
print('Exemplo 2\n')
# Lendo uma planilha excel bem grande com o pandas
vendas_df =  pd.read_excel('planilhas/Vendas.xlsx')
print(vendas_df)

print('################################')
print('Exemplo 3\n')
# Pegando apenas algumas linhas da tabela
print("Primeiras 10 linhas do df: ")
print(vendas_df.head(10))
print("Dimensões da tabela: ")
print(vendas_df.shape)

print('################################')
print('Exemplo 4\n')
# Pegar as colunas númericas e calcula várias coisas, como : quantidade, média, mínimo, desvio padrão, máximo
# e valor dos quartis
print(vendas_df.describe())

print('################################')
print('Exemplo 5\n')
# Para pegar apenas uma coluna especifica para se analisar é bem simples
produtos = vendas_df[['Produto' , 'ID Loja']]
print(produtos)

print('################################')
print('Exemplo 6\n')
# Para pegar linhas especificas, temos diversas formas, alguma delas serão as apresentadas abaixo
print(vendas_df.loc[1:5])

print('################################')
print('Exemplo 7\n')
# Pegar linhas que correspondem a uma condição
print(vendas_df.loc[vendas_df['ID Loja'] == "Norte Shopping"])
#Pode também pegar várias linhas e colunas com o loc
print(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']])


print('################################')
print('Exemplo 8\n')
# É possível adicionar uma coluna em um dataframe da seguinte forma
vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05
print(vendas_df)


print('################################')
print('Exemplo 9\n')
#Com o panda da pra se juntar dois dataframes muito facilmente
#Vamos juntar o dataframe vendas dezembro com o dataframe vendas
vendas = pd.read_excel('planilhas/Vendas.xlsx')
vendas_dezembro = pd.read_excel('planilhas/Vendas - Dez.xlsx')
vendas_df.append(vendas_dezembro)
print(vendas)


print('################################')
print('Exemplo 10\n')
# E por ultimo exclusão de linhas ou colunas do dataframe
vendas_df = vendas_df.drop(["Comissão"], axis=1)
print(vendas_df)

