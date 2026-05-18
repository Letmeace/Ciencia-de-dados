import pandas as pd

from pathlib import Path
import sys

here = Path(__file__).parent
csv_path = here / "produtos.csv"
if not csv_path.exists():
    print(f"Arquivo 'produtos.csv' não encontrado em: {csv_path}")
    print("Coloque o arquivo nessa pasta ou use o caminho absoluto.")
    print("Arquivos no diretório:", [p.name for p in here.iterdir()])
    sys.exit(1)

dados = pd.read_csv(csv_path)
print(dados)

produtos = pd.read_csv("produtos.csv")