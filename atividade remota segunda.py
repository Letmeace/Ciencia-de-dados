import pandas as pd

from pathlib import Path
import sys

here = Path(__file__).parent
csv_path = here / "faturamento_ti.csv"
if not csv_path.exists():
    print(f"Arquivo 'faturamento_ti.csv' não encontrado em: {csv_path}")
    print("Coloque o arquivo nessa pasta ou use o caminho absoluto.")
    print("Arquivos no diretório:", [p.name for p in here.iterdir()])
    sys.exit(1)

dados = pd.read_csv(csv_path)
print(dados)

print(dados.head())

if 'Horas_Suporte' in dados.columns:
    dados['Faturamento'] = 50 * dados['Horas_Suporte'] + 200
    print("\nTotal_Cobrado_R$:")
    print(dados[['Horas_Suporte', 'Faturamento']].head())
else:
    print("\nColuna 'Horas_Suporte' não encontrada. Colunas disponíveis:", list(dados.columns))

media_faturamento = dados['Faturamento'].mean() if 'Faturamento' in dados.columns else 0
print(f"Média de Faturamento: R$ {media_faturamento:.2f}")

cols = ['Cliente', 'Horas_Suporte', 'Faturamento']
available = [c for c in cols if c in dados.columns]
df_final = dados[available].copy()

resumo = {}
if 'Cliente' in df_final.columns:
    resumo['Cliente'] = 'Média'
if 'Horas_Suporte' in df_final.columns:
    resumo['Horas_Suporte'] = df_final['Horas_Suporte'].mean()
if 'Faturamento' in df_final.columns:
    resumo['Faturamento'] = df_final['Faturamento'].mean()

if resumo:
    df_final = pd.concat([df_final, pd.DataFrame([resumo])], ignore_index=True)

export_path = here / "relatorio_ti_final.csv"
df_final.to_csv(export_path, index=False)
print(f"Arquivo exportado para: {export_path}")