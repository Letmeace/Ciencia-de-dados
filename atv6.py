import pandas as pd

df_rede = pd.read_csv('trafego_rede.csv')

media_consumo = df_rede['consumo_gb'].mean()

print("=== Relatório de Infraestrutura: Tráfego de Rede ===")
print(df_rede)
print("-" * 52)
print(f"Média Geral de Consumo da Infraestrutura: {media_consumo:.2f} GB")
print("=" * 52)