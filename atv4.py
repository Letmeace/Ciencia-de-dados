import pandas as pd

inventario = {
    "filial": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"],
    "Usuarios_Ativos": [45, 30, 12, 25, 8]
}
df_custo = pd.DataFrame(inventario)

df_custo["Custo_Total_R$"] = (15 * df_custo["Usuarios_Ativos"]) + 80

print("=== Projeção de Custo de Licenciamento por Filial ===")
print(df_custo)
print("=" * 53)

df_custo.to_csv("custo_licenciamento.csv", index=False)
print("\nArquivo 'custo_licenciamento.csv' gerado com sucesso!")