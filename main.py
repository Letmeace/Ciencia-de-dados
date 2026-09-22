import pandas as pd 

litros_consumidos =pd.Series(
    [120, 300, 250, 410, 670],
    index=['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta']

)

print(litros_consumidos.to_string())
print(litros_consumidos['Quarta'])

precos_originais = pd.Series([10.0, 50.0, 100.0, 150.0, 200.0], index=['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'])

precos_com_aumento = precos_originais * 1.1

print("precos_originais:")
print(precos_originais.to_string())

print("\nprecos com 10% de aumento:")
print(precos_com_aumento.to_string())

dados_pessoas = pd.DataFrame({
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'Idade': [25, 30, 35, 40],
})
print(dados_pessoas.to_string())