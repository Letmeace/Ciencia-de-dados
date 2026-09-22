import pandas as pd

dados_nuvem = {
    "Provedor": ["CloudAlpha", "BetaStorage", "OmegaData"],
    "Preco_Mensal_R$": [150.00, 80.00, 250.00],
    "Espaco_GB": [500, 200, 2000]
}
df_nuvem = pd.DataFrame(dados_nuvem)

df_nuvem["Custo_Por_GB_R$"] = df_nuvem["Preco_Mensal_R$"] / df_nuvem["Espaco_GB"]

print("=== Comparativo de Provedores de Nuvem ===")
print(df_nuvem)
print("=" * 55)

df_nuvem.to_csv("nuvem.csv", index=False)
print("\nArquivo 'nuvem.csv' gerado com sucesso!")