import pandas as pd 

dados_loja =  {
    'Produto': ['Notebook', 'Mouse', 'Teclado'],
    'Preco': [4500.0, 150.0, 1500.0],
    'Estoque': [15, 120, 500]
}

dados_loja = pd.DataFrame(dados_loja)

print(dados_loja.head(2))

print(dados_loja['Produto'])

print(dados_loja[['Produto', 'Preco']])

print(dados_loja[dados_loja['Preco'] < 10])

dados_loja['Valor_total'] = dados_loja['Preco'] * dados_loja['Estoque']

print(dados_loja)









