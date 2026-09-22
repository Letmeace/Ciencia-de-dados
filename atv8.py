import pandas as pd

dados_vendas = {
    "Trimestre": ["T1", "T2", "T3", "T4"],
    "Novos_Projetos": [3, 5, 2, 6]
}
df_vendas = pd.DataFrame(dados_vendas)

df_vendas["Faturamento_Previsto_R$"] = (1200 * df_vendas["Novos_Projetos"]) + 5000

print("=== Projeção de Faturamento Trimestral ===")
print(df_vendas)
print("=" * 45)

df_vendas.to_csv("previsao_faturamento.csv", index=False)
print("\nArquivo 'previsao_faturamento.csv' gerado com sucesso!")