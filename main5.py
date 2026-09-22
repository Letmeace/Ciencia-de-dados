import pandas as pd

filiais = {
    'filial': ['Filial A', 'Filial B', 'Filial C', 'Filial D'],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba'],
    'Faturamento_Milhares': [100000, 150000, 120000, 90000]
}

print(pd.DataFrame(filiais)['Faturamento_Milhares'].describe())

print(pd.DataFrame(filiais)[pd.DataFrame(filiais)['Faturamento_Milhares'] > 100])