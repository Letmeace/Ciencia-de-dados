import pandas as pd

df = pd.read_csv("funcionarios.csv")

df_f = df[df['Tempo_Empresa_Anos'] > 2]

print("="*40)
print(df_f)
print("="*40)