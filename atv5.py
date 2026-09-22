import pandas as pd

df_estoque = pd.read_csv("estoque.csv")

df_alto_custo = df_estoque[df_estoque['Preco_Unitario'] > 500.00]

print("=== Auditoria: Componentes de Alto Custo (> R$ 500) ===")
print(df_alto_custo)
print("=" * 55)

df_alto_custo.to_csv("hardware_alto_custo.csv", index=False)
print("\nArquivo 'hardware_alto_custo.csv' gerado com sucesso!")