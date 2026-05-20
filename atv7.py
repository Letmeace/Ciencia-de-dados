import pandas as pd

dados_notas = {
    "Aluno": ["Arthur", "Bruna", "Caio", "Daniela", "Eduardo"],
    "Nota_Logica": [8.5, 9.0, 6.5, 7.0, 10.0],
    "Nota_Python": [9.0, 8.5, 5.0, 8.0, 9.5]
}

df_alunos = pd.DataFrame(dados_notas)

df_resumo = df_alunos.describe()

print("=== Resumo Estatístico Descritivo ===")
print (df_resumo)
print("=" * 40)

df_resumo.to_csv("resumo_desempenho.csv")
print("\nArquivo 'resumo_desempenho.csv' gerado com sucesso!")