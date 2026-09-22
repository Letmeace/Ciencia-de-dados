import pandas as pd

dados_estudo = {
    "Funcionario": ["Carlos", "Mariana", "Roberto", "Patrícia"],
    "Horas_Dedicadas": [10, 14, 6, 15]
}
df_certificacao = pd.DataFrame(dados_estudo)

df_certificacao["Nota_Projetada"] = (0.5 * df_certificacao["Horas_Dedicadas"]) + 2

print("=== Projeção de Aproveitamento no Simulado ===")
print(df_certificacao)
print("=" * 46)

df_certificacao.to_csv("resultado_certificacoes.csv", index=False)
print("\nArquivo 'resultado_certificacoes.csv' gerado com sucesso!")