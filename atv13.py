import pandas as pd

df_dc = pd.read_csv("data_center.csv")

df_critico = df_dc[df_dc["Temperatura_C"] > 75.0]

print("🚨 [ALERTA] SERVIDORES EM ESTADO CRÍTICO DE SUPERAQUECIMENTO 🚨")
print(df_critico.to_string(index=False))
print("=" * 62)

df_critico.to_csv("manutencao_alerta.csv", index=False)
print("\nArquivo 'manutencao_alerta.csv' gerado com sucesso!")