import pandas as pd

df_logs = pd.read_csv("logs_sistema.csv")

df_critico = df_logs[df_logs["Nivel"] == "CRITICAL"]

print("🚨 [AUDITORIA] FALHAS GRAVES DETECTADAS NO SISTEMA 🚨")
print(df_critico.to_string(index=False))
print("=" * 65)