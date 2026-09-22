import pandas as pd

df_chamados = pd.read_csv("chamados.csv")
pico_maximo = df_chamados["Quantidade_Chamados"].max()
demanda_minima = df_chamados["Quantidade_Chamados"].min()

print("=== Análise Semanal de Volumetria (Help Desk) ===")
print(df_chamados.to_string(index=False))

print("-" * 50)
print(f"O pico máximo de chamados registrado nesta semana foi de {pico_maximo} atendimentos.")
print(f"A demanda mínima de chamados registrada nesta semana foi de {demanda_minima} atendimentos.")
print("=" * 50)