import pandas as pd

dados_inventario = {
    "ID_Equipamento": ["001", "002", "003", "004", "005"],
    "Processador": ["Intel i5", "Intel i5" , "Intel i5" , "Intel i5" , "Intel i5"],
    "Memoria_RAM_GB": [16, 16, 16, 16, 16],
    "Setor": ["Contabilidade", "TI", "RH", "Diretoria", "Marketing"]
}

df_inv = pd.DataFrame(dados_inventario)

print("Visualização do DataFrame criado:")
print(df_inv)
print("-" * 50)

df_inv.to_csv("inventario_ti.csv", index=False)

print("Arquivo 'inventario_ti.csv' gerado com sucesso!")