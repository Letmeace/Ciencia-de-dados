import pandas as pd

df_incidentes = pd.read_csv("incidentes.csv")

df_volumetria = df_incidentes["Tipo_Incidente"].value_counts().reset_index()

df_volumetria.columns = ["Tipo_Incidente", "Quantidade"]

print("=== Ranking de Volumetria de Incidentes ===")
print(df_volumetria.to_string(index=False))
print("=" * 43)

df_volumetria.to_csv("volumetria_seguranca.csv", index=False)
print("\nArquivo 'volumetria_seguranca.csv' gerado com sucesso!")