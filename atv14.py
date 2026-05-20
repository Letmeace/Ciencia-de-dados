import pandas as pd

dados_projetos = {
    "Projeto": ["App Delivery", "E-commerce Premium", "Sistema ERP", "Portal Corporativo"],
    "Valor_Contrato_R$": [85000.00, 120000.00, 250000.00, 45000.00],
    "Custo_Desenvolvimento_R$": [52000.00, 78000.00, 145000.00, 28000.00]
}
df_projetos = pd.DataFrame(dados_projetos)

df_projetos["Lucro_Liquido_R$"] = df_projetos["Valor_Contrato_R$"] - df_projetos["Custo_Desenvolvimento_R$"]

df_projetos["Margem_Lucro_%"] = (df_projetos["Lucro_Liquido_R$"] / df_projetos["Valor_Contrato_R$"]) * 100

print("=== Relatório Financeiro de Lucratividade de Projetos ===")
print(df_projetos)
print("=" * 75)

df_projetos.to_csv("lucratividade_projetos.csv", index=False)
print("\nArquivo 'lucratividade_projetos.csv' gerado com sucesso!")